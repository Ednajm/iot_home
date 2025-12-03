import sqlite3
def init_db():
    conn = sqlite3.connect('smart_home.db')
    c = conn.cursor() 
    c.execute(""" CREATE TABLE IF NOT EXISTS data(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         topic TEXT,
         value REAL,
         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""") 
    conn.commit()
    conn.close()
def save_sensor_data(topic, value):
    conn = sqlite3.connect("smart_home.db")
    c = conn.cursor()
    c.execute("INSERT INTO data (topic, value) VALUES (?, ?)", (topic, value))
    conn.commit()
    conn.close()

def get_last_values():
    conn = sqlite3.connect("smart_home.db")
    c = conn.cursor()
    c.execute("SELECT topic, value, timestamp FROM data ORDER BY id DESC LIMIT 5")
    rows = c.fetchall()
    conn.close()
    return [{"topic": r[0], "value": r[1], "timestamp": r[2]} for r in rows]

    