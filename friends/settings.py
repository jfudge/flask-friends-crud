
import mysql.connector

site_title = "Friends CRUD"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="friends"
)

mycursor = mydb.cursor(dictionary=True, buffered=True)

