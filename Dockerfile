FROM python:3.9-slim

WORKDIR /app

COPY requirements1.txt .
RUN pip install --no-cache-dir -r requirements1.txt

COPY . .

EXPOSE 5000

CMD ["python", "lab1.py"]