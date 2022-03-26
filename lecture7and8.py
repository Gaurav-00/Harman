'''relatioal and                     non relational db
   table                                    {key:value}
 data engine-: MYSQL,sqlite,oracle    MOngoDB,CAsandra
    sql==>lge
    sqlite=>as inbuilt                       

==================
Modules-: are python files
sqlite             python
NULL                None
INTEGER             int
REAL                 float
TEXT                 str
BLOB                  bytes
'''


import sqlite3
con = sqlite3.connect('student.db')
#create cursor object
cursor = con.cursor()

sqlite_query = '''CREATE TABLE stud_marksssssss
                     ( id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        marks INTEGER NOT NULL)'''

cursor.execute(sqlite_query)
print('table created successfully')
sqlite_insert_query='''INSERT INTO stud_marksssssss
                      VALUES(1001,'TOM',95)'''
print('record inserted succesfully')
cursor.execute(sqlite_insert_query)
con.commit()
con.close()