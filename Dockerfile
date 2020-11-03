FROM python:3.8

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src /app/src

CMD ["python", "/app/src/main.py"]
