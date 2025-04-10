
import sqlite3

con = sqlite3.connect("pokemon.db")
print()
print(f"1. Database Setup: \t'pokemon.db'")

with con:
    con.execute("DROP TABLE IF EXISTS adventurers")
    con.execute("""
        CREATE TABLE adventurers 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL, 
             pokemon TEXT NOT NULL, 
             badges INTEGER
            )
    """)
    print(f"2. Table Setup: \t'adventurers'")
    
    
    cur = con.cursor()
    res = cur.execute("""SELECT name from sqlite_master""").fetchall()
    # print(f"3. Tables Existing: \t{res!r}")
    print(f"3. Tables Existing: \t{res!r}")

    cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name='adventurers'")
    for name, sql in cur.fetchall():
        print(f"4. OG Schema {name!r}: \n\t\t\t{sql}")
    print()
    
    cur.execute("PRAGMA table_info(adventurers);")
    print(f"5. Latest Schema {name!r}")
    for col in cur.fetchall():
        print(f"\t\t\t{col}")
    print()
    
    

