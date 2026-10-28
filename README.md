# Finwise — Finance Intelligence Agent

An offline, classroom-focused demo that shows validated transaction data and a bounded subscription-price audit. It uses only fictional data; **do not upload real bank statements**. No payment, email, merchant contact, or money movement is implemented.

## Run it

Backend (Python 3.11+; do **not** use `npm` in this folder):
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Frontend (Node 18+):
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:5173`; API docs are at `http://localhost:8000/docs`.

## Demo flow

1. Load the 14 fictional transactions.
2. Review the dashboard ($364.34 total; $221.34 subscriptions).
3. Run the offline audit.
4. Review the StreamBox Premium 30.0% hike and $588.00 annualized cost.
5. Inspect the trace and generated draft.
6. Approve or reject the simulation. `sent` always remains `false`.

## API

`GET /api/health`, `GET /api/sample`, `POST /api/extract`, `POST /api/audits`, `GET /api/audits/{session_id}`, and `POST /api/audits/{session_id}/approval`.

Extraction intentionally returns 503 offline. `backend/app/ai_service.py` is a documented stub for a future Gemini structured-extraction integration; the API key belongs only in `backend/.env` and is never exposed to the browser. CSV/image/PDF validation, input limits, sessions, and audit trace remain backend-owned.

## Test

```bash
cd backend && pytest
```

## Limits and troubleshooting

Sessions are in memory and reset when the server restarts. The audit only uses allowlisted deterministic operations and treats transaction text as untrusted data. If the browser reports an unavailable backend, start the backend on port 8000 and ensure `FRONTEND_ORIGINS` permits `http://localhost:5173`.
