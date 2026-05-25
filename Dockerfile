FROM python:3.9-slim

WORKDIR /app

# Création d'un utilisateur non-root sécurisé
RUN useradd -m appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# On donne la propriété des fichiers à notre utilisateur
RUN chown -R appuser:appuser /app

# On bascule sur cet utilisateur sécurisé
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
