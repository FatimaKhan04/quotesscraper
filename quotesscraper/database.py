import sqlite3

conn=sqlite3.connect('myquotes.db')
curr=conn.cursor()
curr.execute("""Create table quotes_db(
    quote text,
    author text,
    tag text
    )""")
conn.commit()
conn.close()