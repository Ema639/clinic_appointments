from sqlalchemy.ext.asyncio import AsyncSession
import models as models
import schemas as schemas
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select


async def create_appointment(db: AsyncSession, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(**appointment.model_dump())
    db.add(db_appointment)
    try:
        await db.commit()
        await db.refresh(db_appointment)
        return db_appointment
    except IntegrityError:
        await db.rollback()
        return None


async def get_appointment(db: AsyncSession, appointment_id: int):
    result = await db.execute(select(models.Appointment).where(models.Appointment.id == appointment_id))
    return result.scalars().first()
