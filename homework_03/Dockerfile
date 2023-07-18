FROM python:3.11.3-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==1.5.1"
RUN poetry config virtualenvs.create false --local

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-ansi --only main

COPY blog .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]

EXPOSE 8000

# This container runs with command <<docker run -p 8000:8000 -it app>>
