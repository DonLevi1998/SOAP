FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "hello_soap.py"]  # Reemplaza "hello_soap.py" con el nombre real de tu archivo