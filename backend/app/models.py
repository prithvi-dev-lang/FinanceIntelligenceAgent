from datetime import date, datetime
from decimal import Decimal
from typing import Literal
from pydantic import BaseModel, Field, field_validator

class Transaction(BaseModel):
    id: str
    date: date
    merchant: str = Field(min_length=1, max_length=120)
    category: Literal['Subscriptions', 'Groceries', 'Coffee', 'Other']
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    raw_source: str = Field(min_length=1, max_length=1000)
    @field_validator('merchant', 'raw_source')
    @classmethod
    def clean(cls, value): return value.strip()

class Statement(BaseModel):
    transactions: list[Transaction] = Field(max_length=500)

class AuditRequest(BaseModel):
    transactions: list[Transaction] = Field(min_length=1, max_length=500)

class ApprovalRequest(BaseModel):
    decision: Literal['approve', 'reject']

class TraceEvent(BaseModel):
    timestamp: datetime
    event: str
    detail: str

class HikeFinding(BaseModel):
    merchant: str
    previous_amount: Decimal
    current_amount: Decimal
    increase_percent: Decimal
    detected_on: date

class AgentDecision(BaseModel):
    action: Literal['detect_stealth_hikes', 'calculate_annualized_cost', 'generate_draft', 'finish']
    arguments: dict = Field(default_factory=dict)
