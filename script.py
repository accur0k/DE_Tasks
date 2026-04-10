import re
import json
import psycopg2

with open("task1_d.json", "r", encoding="utf-8") as f:
    raw = f.read()

raw = re.sub(r':(\w+)=>', r'"\1":', raw)
raw = raw.replace("&amp;", "&")

data = json.loads(raw)

conn = psycopg2.connect(dbname="study", user="postgres", password="123", host="localhost")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id NUMERIC PRIMARY KEY,
        title VARCHAR(100),
        author VARCHAR(100),
        genre VARCHAR(50),
        publisher VARCHAR(100),
        year INT,
        price VARCHAR(10)
    )
""")

for row in data:
    cur.execute(
        "INSERT INTO books (id, title, author, genre, publisher, year, price) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
        (row["id"], row["title"], row["author"], row["genre"], row["publisher"], row["year"], row["price"])
    )

conn.commit()
cur.close()
conn.close()

print(f"Records: {len(data)}")