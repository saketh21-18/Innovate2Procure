<<<<<<< HEAD
# Innovate2Procure

A startup-friendly innovation procurement prototype for government departments.

## Features
- Premium SaaS-style landing page matching the project UI mockups
- Government dashboard
- Login / registration with name, email, department and role
- Host/Admin dashboard that receives submitted participant details
- SQLite persistence
- Innovation workflow: Define → Discover → Evaluate → Pilot → Prove → Scale
- Responsive interface

## Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python + Flask
Database: SQLite

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Host demo

Choose `Host / Admin` during login. Every submitted participant is saved in `innovate2procure.db` and shown in the Host Overview.

## Important

This is a college-project prototype. For real deployment, use proper authentication/password hashing or SSO, HTTPS, role-based permissions, a production database, audit logging, privacy/retention controls and security review before collecting real personal or government data.
=======
# Innovate2Procure
>>>>>>> 691c8f115d095737147494a8f47b120824be5d56
