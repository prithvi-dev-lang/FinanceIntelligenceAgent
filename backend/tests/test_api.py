from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_sample_metrics_and_audit():
    data = client.get('/api/sample').json()['transactions']
    assert len(data) == 14 and sum(float(x['amount']) for x in data) == 364.34
    session = client.post('/api/audits', json={'transactions': data}).json()
    assert session['status'] == 'awaiting_approval' and session['annualized_cost'] == 588.0
    assert client.post(f"/api/audits/{session['id']}/approval", json={'decision':'approve'}).json()['sent'] is False
    assert client.post(f"/api/audits/{session['id']}/approval", json={'decision':'approve'}).status_code == 409
