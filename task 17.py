import sqlite3
conn= sqlite3.connect("employe.db")
print("opened database successfully")
print(sqlite3.sqlite_version)
conn.execute("CREATE TABLE students(nameTEXT,addr TEXT,cityTEXT,pinTEXT)")
print("Table created successfully")
conn.close()