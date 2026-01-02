from database import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXIST visits (
        id TEXT PRIMARY KEY,
        date TEXT NOT NULL,
        spec TEXT NOT NULL,
        visiter TEXT NOT NULL,
        issues TEXT NOT NULL,
        delegation TEXT NOT NULL,
        result TEXT NOT NULL,
        deleted INTEGER DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()