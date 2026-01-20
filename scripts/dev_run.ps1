# Quick run for Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# routing server
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "-m","uvicorn","services.routing_server.app.main:app","--reload","--port","8000"

# admin server
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "-m","uvicorn","services.admin_server.app.main:app","--reload","--port","8001"
