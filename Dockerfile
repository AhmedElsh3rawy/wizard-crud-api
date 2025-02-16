From python:3.8-slim

RUN apt-get update && apt-get install -y libpq-dev gcc # required by psycopg2

RUN pip install fastapi uvicorn sqlalchemy psycopg2

WORKDIR /app

COPY . .

EXPOSE 8080

CMD [ "python", "init_db.py" ]

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]
