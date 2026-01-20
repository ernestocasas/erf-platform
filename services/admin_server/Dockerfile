FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY packages/shared /app/packages/shared
COPY services/admin_server /app/services/admin_server

ENV PYTHONPATH=/app/packages/shared

EXPOSE 8001
CMD ["uvicorn", "services.admin_server.app.main:app", "--host", "0.0.0.0", "--port", "8001"]
