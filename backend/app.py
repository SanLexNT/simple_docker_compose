from flask import Flask
import os
import psycopg2

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from Backend!"


@app.route("/db")
def db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=int(os.getenv("DB_PORT", 5432)),
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]

        cur.close()
        conn.close()

        return f"Connected to PostgreSQL!<br><br>{version}"

    except Exception as e:
        return f"Database connection failed:<br><br>{e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)