from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3, os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-this")
if os.environ.get("VERCEL"):
    DB = os.environ.get("DATABASE_PATH", "/tmp/innovate2procure.db")
else:
    DB = os.environ.get(
        "DATABASE_PATH",
        os.path.join(os.path.dirname(__file__), "innovate2procure.db")
    )

def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = db()
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        department TEXT NOT NULL,
        role TEXT NOT NULL,
        created_at TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        department = request.form.get("department", "").strip()
        role = request.form.get("role", "department").strip()

        if not name or not email or not department:
            return render_template("login.html", error="Please complete all required fields.")

        conn = db()
        conn.execute(
            "INSERT INTO users(name,email,department,role,created_at) VALUES (?,?,?,?,?)",
            (name, email, department, role, datetime.utcnow().isoformat(timespec="seconds"))
        )
        conn.commit()
        conn.close()

        session["name"] = name
        session["role"] = role
        session["department"] = department
        return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "name" not in session:
        return redirect(url_for("login"))
    return render_template(
        "dashboard.html",
        name=session["name"],
        role=session["role"],
        department=session["department"]
    )

@app.route("/host")
def host():
    if session.get("role") != "host":
        return redirect(url_for("login"))
    conn = db()
    users = conn.execute("SELECT * FROM users ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("host.html", users=users)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/api/users")
def api_users():
    if session.get("role") != "host":
        return jsonify({"error": "Unauthorized"}), 403
    conn = db()
    users = [dict(row) for row in conn.execute("SELECT * FROM users ORDER BY id DESC").fetchall()]
    conn.close()
    return jsonify(users)

@app.before_request
def ensure_database():
    # Vercel serverless instances are ephemeral; /tmp is the writable area.
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
