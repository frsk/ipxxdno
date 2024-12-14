FROM python:3-alpine

EXPOSE 8080

WORKDIR /app

COPY gunicorn_config.py .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ipxxdno.py .

USER nobody

ENV IP_HEADER False

CMD ["gunicorn", "--config", "gunicorn_config.py", "-b", "[::]:8080", "ipxxdno:app"]
