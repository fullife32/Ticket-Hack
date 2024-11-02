from dataclasses import dataclass
from datetime import datetime
import uuid
from flask import jsonify


@dataclass
class FakeTicket:
    def __init__(self, price: int, event_name: str, event_date: datetime, consumed: bool = False):
        self.price = price
        self.event_name = event_name
        self.event_date = event_date
        self.consumed = consumed
        self.id = uuid.uuid4()

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "event_name": self.event_name,
            "event_date": self.event_date,
            "consumed": self.consumed,
        }
