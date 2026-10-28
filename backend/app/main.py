import os
from decimal import Decimal
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from .models import Statement, AuditRequest, ApprovalRequest, Transaction
from .sample_data import SAMPLE_TRANSACTIONS
from .audit import start_audit, SESSIONS, decide

app = FastAPI(title='Finwise Finance Intelligence Agent')
origins = os.getenv('FRONTEND_ORIGINS', 'http://localhost:5173').split(',')
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=False, allow_methods=['*'], allow_headers=['*'])

@app.get('/api/health')
def health(): return {'status': 'ok', 'gemini_configured': bool(os.getenv('GEMINI_API_KEY')), 'mode': 'offline'}
@app.get('/api/sample', response_model=Statement)
def sample(): return Statement(transactions=SAMPLE_TRANSACTIONS)
@app.post('/api/extract', response_model=Statement)
async def extract(text: str | None = Form(None), file: UploadFile | None = File(None)):
    if not text and not file: raise HTTPException(422, 'Provide pasted text or a file.')
    if text and len(text) > 100000: raise HTTPException(413, 'Text exceeds 100,000 characters.')
    if file:
        if file.content_type not in {'text/csv', 'text/plain', 'application/pdf', 'image/png', 'image/jpeg'}: raise HTTPException(415, 'Unsupported file type.')
        data = await file.read()
        if len(data) > 12 * 1024 * 1024: raise HTTPException(413, 'File exceeds 12 MB.')
    raise HTTPException(503, 'Extraction needs a future Gemini integration. Load fictional sample data for offline mode.')
@app.post('/api/audits')
def audits(request: AuditRequest): return start_audit(request.transactions)
@app.get('/api/audits/{session_id}')
def audit(session_id: str):
    if session_id not in SESSIONS: raise HTTPException(404, 'Audit session not found.')
    return SESSIONS[session_id]
@app.post('/api/audits/{session_id}/approval')
def approval(session_id: str, request: ApprovalRequest):
    session, error = decide(session_id, request.decision)
    if error == 'missing': raise HTTPException(404, 'Audit session not found.')
    if error == 'conflict': raise HTTPException(409, 'Audit is not awaiting approval.')
    return session
