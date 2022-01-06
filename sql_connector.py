import mysql.connector as m
mydb=m.connect(host="localhost",user="Sayantan",passwd="sayantan741101",database="users")
mycursor=mydb.cursor()
mycursor.execute("select * from Users")
result=mycursor.fetchall()
for i in result:
 print(i)