#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Starting routing_server on :8000"
uvicorn services.routing_server.app.main:app --reload --port 8000 &

echo "Starting admin_server on :8001"
uvicorn services.admin_server.app.main:app --reload --port 8001 &

wait
