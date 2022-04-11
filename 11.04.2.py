import sqlite3

db = sqlite3.connect('test.db')

db.execute("""CREATE TABLE IF NOT EXISTS sastavdalas
    (id         INTEGER     PRIMARY  KEY AUTOINCREMENT,
    pirma CHAR(50)     NOT NULL,
    otra   CHAR(50),
    tresa  CHAR(50)
    )""") 

pirma = input("Pirma sastavdala:")
otra = input("Otra sastavdala:")
tresa = input("Tresa sastavdala:")

db.execute("""INSERT INTO sastavdalas
            (pirma,otra,tresa)
            VALUES (:pirma,:otra,:tresa)
""",{'pirma':pirma,'otra':otra,'tresa':tresa})

db.commit()

dati = db.execute("SELECT * FROM sastavdalas")

print(dati)
rezultats = dati.fetchall()
#print(rezultats)
for rinda in rezultats:
  print("ID: ",rinda[0])
  print("1 sastavdala: ",rinda[1])
  print("2 sastavdala: ",rinda[2])