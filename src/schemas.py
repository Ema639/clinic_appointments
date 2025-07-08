from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    patient_name: str
    doctor_id: int
    start_time: datetime

class AppointmentOut(AppointmentCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True