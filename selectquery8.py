import sqlite3
con = sqlite3.connect('student.db')
cursor=con.cursor()
#1st method to fetch all record
sqlite_select_query='''SELECT * FROM stud_marksssssss'''

cursor.execute(sqlite_select_query)
records=cursor.fetchall()
#2 nd method to fetch all record
for row in records:
    print('id:',row[0])
    print('name:',row[1])
    print('marks:',row[2])

print(records)
con.close()