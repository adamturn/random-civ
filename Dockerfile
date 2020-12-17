FROM python:3.6

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY src /app/src

CMD [ "python", "/app/src/main.py", "update" ]
