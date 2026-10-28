from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
from .models import Transaction, HikeFinding

def detect_stealth_hikes(transactions: list[Transaction], threshold: Decimal = Decimal('0.10')) -> list[HikeFinding]:
    """Compare each subscription with its immediately previous charge."""
    by_merchant = defaultdict(list)
    for tx in transactions:
        if tx.category == 'Subscriptions': by_merchant[tx.merchant].append(tx)
    findings = []
    for merchant, rows in by_merchant.items():
        rows.sort(key=lambda x: x.date)
        for prev, current in zip(rows, rows[1:]):
            change = (current.amount - prev.amount) / prev.amount
            if change > threshold:
                findings.append(HikeFinding(merchant=merchant, previous_amount=prev.amount, current_amount=current.amount,
                    increase_percent=(change * 100).quantize(Decimal('0.1')), detected_on=current.date))
    return findings

def calculate_annualized_cost(monthly_amount: Decimal) -> Decimal:
    return (monthly_amount * 12).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def generate_draft(finding: HikeFinding, annualized_cost: Decimal) -> str:
    return (f"Subject: Request to review my {finding.merchant} price increase\n\n"
            f"Hello {finding.merchant}, I noticed my monthly price changed from ${finding.previous_amount:.2f} "
            f"to ${finding.current_amount:.2f}. Please explain the change or help me cancel. "
            f"The current annualized cost is ${annualized_cost:.2f}.\n\nThank you.")
