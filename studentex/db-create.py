import sqlite3

db_locale = 'students.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor()

c.execute("""
CREATE TABLE contact
(id INTEGER PRIMARY KEY AUTOINCREMENT,
firstname TEXT,
lastname TEXT,
street_address TEXT,
suburb TEXT
)
""")


connie.commit()
connie.close()
