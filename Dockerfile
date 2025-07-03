# Используем официальный Python
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["gunicorn", "project_core.wsgi", "--bind", "0.0.0.0:$PORT"]