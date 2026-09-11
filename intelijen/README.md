# INTELIJEN

INTELIJEN is a minimal foundation for an OSINT and public information analysis application.

## Project overview

This phase implements a minimal FastAPI backend, a lightweight HTML/CSS/JavaScript frontend, and a health check endpoint required by the Phase 1 foundation.

## Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment:

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run backend

```bash
uvicorn backend.main:app --reload
```

The backend will be available at:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## Run tests

```bash
pytest
```

## Health check endpoint

```http
GET /api/health
```

Response:

```json
{
  "status": "ok",
  "application": "INTELIJEN",
  "version": "0.1.0"
}
```
