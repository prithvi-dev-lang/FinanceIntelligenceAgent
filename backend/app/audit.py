from datetime import datetime, timezone
from decimal import Decimal
from uuid import uuid4
from .models import Transaction
from .tools import detect_stealth_hikes, calculate_annualized_cost, generate_draft

SESSIONS = {}
def _event(session, event, detail):
    session['trace'].append({'timestamp': datetime.now(timezone.utc).isoformat(), 'event': event, 'detail': detail})

def start_audit(transactions: list[Transaction]):
    """Bounded three-operation offline planner; no arbitrary tool execution."""
    session = {'id': str(uuid4()), 'status': 'running', 'sent': False, 'decision': None, 'findings': [], 'draft': None, 'annualized_cost': None, 'trace': []}
    _event(session, 'plan', 'Offline planner started: detect, price, draft, await approval.')
    findings = detect_stealth_hikes(transactions)
    session['findings'] = [x.model_dump(mode='json') for x in findings]
    _event(session, 'detect_stealth_hikes', f'Found {len(findings)} qualifying increase(s).')
    if findings:
        cost = calculate_annualized_cost(findings[0].current_amount)
        session['annualized_cost'] = float(cost)
        _event(session, 'calculate_annualized_cost', f'Annualized current cost: ${cost:.2f}.')
        session['draft'] = generate_draft(findings[0], cost)
        _event(session, 'generate_draft', 'Generated a review/cancellation draft; no message was sent.')
    session['status'] = 'awaiting_approval'
    _event(session, 'awaiting_approval', 'Human decision required before simulated action is recorded.')
    SESSIONS[session['id']] = session
    return session

def decide(session_id: str, decision: str):
    session = SESSIONS.get(session_id)
    if not session: return None, 'missing'
    if session['status'] != 'awaiting_approval': return None, 'conflict'
    session['decision'] = decision
    session['status'] = 'approved' if decision == 'approve' else 'rejected'
    _event(session, 'decision', f'Simulated {decision}; no external message was sent.')
    return session, None
