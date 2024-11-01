from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime


@dataclass_json
@dataclass
class Ticket:
    ticket_numbers: int
    event_name: str
    unary_price: float
    event_date: datetime
