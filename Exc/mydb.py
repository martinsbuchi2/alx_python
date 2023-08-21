import sqlite3

db = sqlite3.connect("mydb.db")

cursor = db.cursor()

#cursor.execute("""CREATE TABLE IF NOT EXISTS employee (
#    SN INT PRIMARY KEY,
#    f_name VARCHAR (200),
#    l_name VARCHAR (200),
#    age INT
#    )""")

#cursor.execute('INSERT INTO employee VALUES(1,"Raj","Kumar",45)')

cursor.execute("SELECT * FROM employee WHERE l_name='Kumar'")



db.commit()
db.close()