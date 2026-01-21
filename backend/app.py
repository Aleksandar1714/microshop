import os
import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
DB_NAME = os.environ.get("DB_NAME", "microshop")
DB_USER = os.environ.get("DB_USER", "microshop")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "microshoppass")


def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


@app.get("/health")
def health():
    try:
        conn = get_conn()
        conn.close()
        return {"status": "ok"}
    except Exception as e:
        return {"status": "db_error", "detail": str(e)}, 500


@app.get("/items")
def list_items():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, created_at FROM items ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    data = [{"id": r[0], "name": r[1], "created_at": r[2].isoformat()} for r in rows]
    return jsonify(data)


@app.post("/items")
def create_item():
    body = request.get_json(silent=True) or {}
    name = (body.get("name") or "").strip()
    if not name:
        return {"error": "name is required"}, 400

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO items(name) VALUES(%s) RETURNING id, name, created_at;", (name,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": row[0], "name": row[1], "created_at": row[2].isoformat()}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
