''' to insert single record at once
import sqlite3
def insertdata(id,name,marks):
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    #parameterized query
    insert_query='''INSERT INTO stud_marksssssss
                      VALUES(?,?,?)'''

    cursor.execute(insert_query,(id,name,marks))
    con.commit()
    
    con.close()
   

#take input from user
d=int(input("enter number of student you want to add"))
for i in range(d):
    print('add the new details')
    a=int(input("enter the number-:"))
    b=input('enter your name-:')
    c=int(input('enter your marks-:'))
    print('added successfully enter ')
    insertdata(a,b,c)
'''

#to insert Multiple record at once
import sqlite3
def insertmultipledata(Datalist):     #you have to pass just a data list
    con=sqlite3.connect('student.db')
    cursor=con.cursor()
    #parameterized query
    insert_query='''INSERT INTO stud_marksssssss VALUES(Datalist)'''

    cursor.executemany(insert_query,Datalist)  #instead of execute use execute many
    con.commit()
    
    print('to get total count of records',cursor.rowcount)
    con.commit()

    con.close()
   

#give multiple input at once
    Datalist=[(6,'rajesh',77),(7,'fr'.89),(9,'tr',99)]
    insertmultipledata(Datalist)
