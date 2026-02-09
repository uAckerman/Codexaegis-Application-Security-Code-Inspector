from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

@app.route("/", methods=["GET"])
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # INTENTIONALLY VULNERABLE
    query = f"""
        SELECT * FROM users
        WHERE username = '{username}'
        AND password = '{password}'
    """

    cur.execute(query)
    user = cur.fetchone()
    conn.close()

    if user:
        return render_template("login.html", message="✅ Login successful")
    else:
        return render_template("login.html", message="❌ Invalid username or password")

if __name__ == "__main__":
    app.run(debug=True)
