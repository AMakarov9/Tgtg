import sqlite3
class Butikk: 
    def __init__(self, navn):
        self._navn = navn
        self.connection = sqlite3.connect("tgtg.db")
        self.cursor = self.connection.cursor()
    
    def legg_til_butikk(self): 
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self._navn} (
            day SMALLINT NOT NULL,
            tid TIME NOT NULL
        )""")

    def legg_til_tid(self, dag, tid): 
        self.cursor.execute(f"""INSERT INTO {self._navn} VALUES (
            {dag}, '{tid}'
        )""")
        self.connection.commit()



 