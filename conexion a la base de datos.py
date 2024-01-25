import mysql.connector

#Establecemos la conexion a la base de datos "ahorcado"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="stitch2012",
  database="ahorcado"

)

cursor = mydb.cursor()
cursor.execute("SHOW TABLES")
for table in cursor:
  print(table)