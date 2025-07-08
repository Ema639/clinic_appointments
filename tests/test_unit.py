import pytest
from unittest.mock import AsyncMock
from src import schemas, crud


@pytest.mark.asyncio
async def test_create_appointment_success():
    db = AsyncMock()
    appointment = schemas.AppointmentCreate(
        patient_name="Test Patient",
        doctor_id=1,
        start_time="2030-01-01T10:00:00",
    )

    db.commit.return_value = None
    db.refresh.return_value = None

    db.add.return_value = None

    result = await crud.create_appointment(db, appointment)

    assert result is not None
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()
