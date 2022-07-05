FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

COPY ./.env /app/.env

RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "saba:app"]