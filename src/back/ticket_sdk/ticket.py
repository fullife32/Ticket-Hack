from dataclasses import dataclass
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, confloat, conint, constr, validator

from ticket_sdk.fake_ticket import FakeTicket


class TicketEmitterDto(BaseModel):
    ticket_numbers: conint(gt=0)
    event_name: constr(min_length=3, max_length=100)
    unary_price: confloat(gt=0.1)
    event_date: datetime = Field(..., description="Date must be in the future")

    @validator("event_date")
    def check_event_date_in_future(cls, v):
        if v <= datetime.now():
            raise ValueError("Date must be set to future")
        return v

class TicketsManager:
    def __init__(self):
        self.emitters = {}

    def emit(self, ticket_emitter_dto: TicketEmitterDto) -> List[FakeTicket]:
        tickets = []

        for _ in range(ticket_emitter_dto.ticket_numbers):
            ticket = FakeTicket(
                ticket_emitter_dto.unary_price,
                ticket_emitter_dto.event_name,
                ticket_emitter_dto.event_date,
                False,
            )
            tickets.append(ticket)

        self.emitters["emitter"] = tickets
        return tickets

    def get_tickets(self, emitter) -> List[FakeTicket]:
        return self.emitters[emitter]
