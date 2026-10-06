# Innovate2Procure

Startup-friendly innovation procurement prototype for government departments.

## Vercel deployment

The project uses `api/index.py` as the Vercel Python entry point and routes all requests to the Flask application.

The prototype uses SQLite. On Vercel, SQLite is stored under `/tmp` because the deployed filesystem is ephemeral. This is suitable for a demo but not for permanent production data. Use a hosted PostgreSQL database for real deployment.

## Local run

```bash
pip install -r requirements.txt
python app.py
```

The existing `templates/` and `static/` folders are required.

## Security

This is a college-project prototype. Before collecting real personal or government data, add proper authentication, protected admin access, HTTPS, production database, audit logging, privacy/retention controls and security review.
