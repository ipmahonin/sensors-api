FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 👇 ВОТ ЭТО ВАЖНО
RUN apt-get update && apt-get install -y postgresql-client

COPY . .

COPY run_migrations.sh .
RUN chmod +x run_migrations.sh

CMD ["sh", "run_migrations.sh"]