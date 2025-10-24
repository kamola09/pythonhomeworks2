
import sqlite3
conn=sqlite3.connect("my_database")

cursor=conn.cursor()

cursor.execute(
    """ create table if  not exists Roster(
     Name TEXT,
    Species TEXT,
    Age INTEGER)

"""

)
conn.commit()
conn.close()
print("sucessfully")


import sqlite3
conn=sqlite3.connect("my_database")
cursor=conn.cursor()
data=[

    
("Benjamin Sisko",  "Human",40),
("Jadzia Dax",  "Trill",300),
("Kira Nerys",  "Bajoran",  29)

]
cursor.executemany("Insert into Roster(Name,Species,Age) Values  (?, ?, ?)",data)
conn.commit()
conn.close()
print("Muvaffaqiyatli qowildi")


import sqlite3
conn=sqlite3.connect("my_database")
cursor=conn.cursor()
cursor.execute("""
    update roster
    set Name='Ezri Dax'
WHERE Name = 'Jadzia Dax'
    """
)
conn.commit()
cursor.execute("select* from roster")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()


import sqlite3
conn=sqlite3.connect("my_database")
cursor=conn.cursor()
cursor.execute(
    """
select name,age from Roster
where species="Bajoran"
"""
)
conn.commit()
cursor.execute("""
               select * from Roster""")

rows=cursor.fetchall()
for row in rows:
    print(row)
