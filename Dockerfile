FROM python:3.9-slim

WORKDIR /app

RUN useradd -m appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#any way
COPY app.py .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
