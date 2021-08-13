import mysql.connector

myuser = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

mycursor = myuser.cursor(buffered=True)

create_db = "CREATE DATABASE `friends`"
mycursor.execute(create_db)

for database in mycursor:
  print(database)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="friends"
)

mycursor = mydb.cursor(buffered=True)

create_table = "CREATE TABLE `friends` (id BIGINT AUTO_INCREMENT PRIMARY KEY, `name` VARCHAR(255), `image` VARCHAR(255), `invited` TINYINT(1))"
mycursor.execute(create_table)
