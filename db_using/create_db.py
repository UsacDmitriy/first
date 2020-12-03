import sqlite3

conn = sqlite3.connect('sqlite/students_db.db')
cursor = conn.cursor()

# cursor.execute("CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER)")
#
# first_name = 'Lily'
# last_name = 'Block'
# age = 23
#
# students =[
#     ('Joe', 'Moses', 21),
#     ('Jeff', 'Green', 20),
#     ('Jacklin', 'Brown', 19),
# ]
#
# jane = ('Jane', 'Air', 21)
# SQL injection!!!
# insert_query = f'INSERT INTO students  VALUES ("{first_name}", "{last_name}", "{age}")'

# insert_query = 'INSERT INTO students  VALUES (?, ?, ?)'
# cursor.execute(insert_query, (first_name, last_name, age))
# cursor.execute(insert_query, jane)

# for student in students:
#     cursor.execute(insert_query, student)

# cursor.executemany(insert_query,students)

# cursor.execute("SELECT * FROM students WHERE first_name = 'Jane';")
#
# for row in cursor:
#     print(row)
cursor.execute("UPDATE students SET last_name = 'Austin' WHERE first_name = 'Jack';")
cursor.execute('SELECT * FROM students;')

data = cursor.fetchall()
[print(row) for row in data]

# print(cursor.fetchone())
# print(cursor.fetchall())


conn.commit()

conn.close()
