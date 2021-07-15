import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="arun")

mycursor = mydb.cursor()

mycursor.execute("DELETE FROM student WHERE name = 'john'")


mydb.commit()