FROM python:3.12-slim

WORKDIR /app

RUN adduser --disabled-password app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
