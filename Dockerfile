FROM python:3.7
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY src /app/src
CMD ["python", "/app/src/main.py", "update"]
