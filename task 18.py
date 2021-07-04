import sqlite3

conn = sqlite3.connect('te12.db')
print("Opened database successfully");
print(sqlite3.sqlite_version)
tab = "CREATE TABLE doct (id INT NOT NULL PRIMARY KEY, patients  VARCHAR(40))"
conn.execute(tab)
print("Table created successfully");
val = [ (1, '6'),
        (2, '4'),
        (3, '3'),
        (4, '7'),
        ]
conn.executemany('INSERT INTO doct VALUES(?,?);',val);
sql = "SELECT * FROM doct"
sql_cursor=conn.execute(sql)
rst = conn.fetchall(sql_cursor)
for x in rst:
    print(x);
conn.commit()
conn.close()