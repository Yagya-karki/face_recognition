import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='text@12345',database='face_recognizer')
my_cursor=conn.cursor()
conn.commit()
conn.close()

print("connection successfully created")