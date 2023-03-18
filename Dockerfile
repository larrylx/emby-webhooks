FROM python:3.9

WORKDIR /app

COPY app.py /app/
COPY templates /app/templates/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8099

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8099", "app:app"]