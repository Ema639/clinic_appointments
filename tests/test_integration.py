import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app


@pytest.mark.asyncio
async def test_create_and_get_appointment():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        data = {"patient_name": "John", "doctor_id": 1, "start_time": "2030-01-01T10:00:00"}
        response = await ac.post("/appointments", json=data)
        assert response.status_code == 200
        appointment_id = response.json()["id"]

        response = await ac.get(f"/appointments/{appointment_id}")
        assert response.status_code == 200
        assert response.json()["patient_name"] == "John"
