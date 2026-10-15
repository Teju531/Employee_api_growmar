FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir fastapi "uvicorn[standard]" pydantic-settings sqlalchemy alembic "psycopg[binary]" python-dotenv pytest httpx email-validator

COPY app ./app
COPY migrations ./migrations
COPY alembic.ini .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
