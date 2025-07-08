from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from database import Base
from datetime import datetime, timezone


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, nullable=False)
    doctor_id = Column(Integer, nullable=False)
    start_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        UniqueConstraint('doctor_id', 'start_time', name='uq_doctor_start_time'),
    )
