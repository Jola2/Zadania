import mysql.connector
from SQL.settings import user, password

connection = mysql.connector.connect(host='localhost',
                                     database='sales',
                                     user=user,
                                     password=password)

print(connection.is_connected())
