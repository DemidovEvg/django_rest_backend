FROM python:3.11

RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev
RUN pip3 install --upgrade pip
COPY wait-for-postgres.sh .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN chmod +x wait-for-postgres.sh
RUN pip3 install gunicorn