from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel, Field, confloat, conint, constr, validator


class Ticket(BaseModel):
    ticket_numbers: conint(gt=0)
    event_name: constr(min_length=3, max_length=100)
    unary_price: confloat(gt=0.1)
    event_date: datetime = Field(..., description="Date must be in the future")

    @validator("event_date")
    def check_event_date_in_future(cls, v):
        if v <= datetime.now():
            raise ValueError("Date must be set to future")
        return v
