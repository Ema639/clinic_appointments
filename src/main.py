from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_session, init_models
import crud as crud
import schemas as schemas
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_models()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok"}


async def get_db():
    async with async_session() as session:
        yield session


@app.post("/appointments", response_model=schemas.AppointmentOut)
async def create_appointment(appointment: schemas.AppointmentCreate, db: AsyncSession = Depends(get_db)):
    db_appointment = await crud.create_appointment(db, appointment)
    if not db_appointment:
        raise HTTPException(status_code=400, detail="Doctor is busy at this time")
    return db_appointment


@app.get("/appointments/{appointment_id}", response_model=schemas.AppointmentOut)
async def get_appointment(appointment_id: int, db: AsyncSession = Depends(get_db)):
    db_appointment = await crud.get_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment
