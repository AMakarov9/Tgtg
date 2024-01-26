
import sqlite3
butikk = "Bussterminalen"
connection = sqlite3.connect("tgtg.db")
cursor = connection.cursor()
for i in ["banan", "eple", "pære"]: 
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {i} (
        day SMALLINT NOT NULL,
        tid TIME NOT NULL
    )""")


    cursor.execute(f"""INSERT INTO {butikk} VALUES (
        1, '10:01'
    )""")

    cursor.execute(f"""SELECT * FROM {butikk}""")

rows = cursor.fetchall()
print(rows)
connection.commit()
connection.close()
