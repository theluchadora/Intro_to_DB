import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",     
        user="root",          
        password="Mysql1!!Pass"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")


except mysql.connector.Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'mycursor' in locals() and mycursor:
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
