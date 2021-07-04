import csv
import _sqlite3

conn = _sqlite3.connect("employee.db")
mycursor = conn.cursor()
print("opened database successfully")
print(_sqlite3.sqlite_version)
tab = """CREATE TABLE employee(id INT NOT NULL PRIMARY KEY, name VARCHAR, salary INT NOT NULL PRIMARY KEY)"""
mycursor.execute(tab)


for row in csv.reader(open('employee.csv', 'r'), delimiter=','):
 if row:
  val1 = row[0]
  val2 = row[1]
  val3 = row[2]
  # print(val)
  mycursor.execute("INSERT INTO employee VALUES(?,?,?)", (val1, val2, val3))
  # mycursor.execute(sql, val)
  mycursor.execute("SELECT * FROM employee")
  result = mycursor.fetchall()
  print(result)