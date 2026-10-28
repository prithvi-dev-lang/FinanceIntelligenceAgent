from decimal import Decimal
from app.sample_data import SAMPLE_TRANSACTIONS
from app.tools import detect_stealth_hikes, calculate_annualized_cost

def test_detects_only_streambox_hike():
    findings = detect_stealth_hikes(SAMPLE_TRANSACTIONS)
    assert len(findings) == 1
    assert findings[0].merchant == 'StreamBox Premium'
    assert findings[0].increase_percent == Decimal('30.0')

def test_annualized_cost(): assert calculate_annualized_cost(Decimal('49.00')) == Decimal('588.00')
