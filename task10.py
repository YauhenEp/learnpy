import sqlite3

# SQLite3

# connection = sqlite3.connect('test.db')
# cursor = connection.cursor()

# if table not in cursor:
# cursor.execute("CREATE TABLE people (first_name text, last_name text, age real)")
# cursor.execute("INSERT INTO people VALUES ('John', 'Doe', 32)")
#
# connection.commit()
# cursor.execute("SELECT * FROM people")
#
# result = cursor.fetchall()
# print(result)
# cursor.close()
# connection.close()

# ODBC
import pyodbc

connection = pyodbc.connect('Driver=SQLite3 ODBC Driver;Database=test.db')
cursor = connection.cursor()
cursor.execute('select * from people')
for row in cursor:
    print(row)

connection.close()