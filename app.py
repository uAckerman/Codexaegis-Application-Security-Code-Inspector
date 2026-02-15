from flask import Flask, request, render_template
import sqlite3 # to interact with the SQLite database.
import os # to check if the database file already exists.

app = Flask(__name__) # application instance is created.

DATABASE = "database.db"

# Initialize Database
# This function is responsible for setting up the database when the application runs for the first time.
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        """)

        # Insert default user
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
        conn.commit()
        conn.close()

init_db() # The function is called immediately so the database is initialized before handling any requests.

@app.route("/") # root URL, Welcome Page
def home():
    return "<h2>Welcome to Vulnerable App</h2><a href='/login'>Login</a>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # INTENTIONALLY VULNERABLE QUERY
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = cursor.execute(query).fetchone()

        conn.close()

        if result:
            return "<h3>Login Successful!</h3>"
        else:
            return "<h3>Invalid Credentials</h3>"

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)

