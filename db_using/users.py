import sqlite3

conn = sqlite3.connect('sqlite/users_db.db')

# create_query = "CREATE TABLE users (user_name TEXT, user_password TEXT)"


users = [
    ('jack123', 'amcancnac'),
    ('jane122321', 'hvjkasipbvfpadi'),
    ('bobman33423', 'jkij[ioj[ioj')
]
# insert_query = 'INSERT INTO users  VALUES (?, ?)'

user_name = input('Input your user name')
user_password = input('Enter password')

select_query = f" SELECT * FROM users WHERE user_name = '{user_name}' AND user_password = '{user_password}'"
cursor = conn.cursor()

# cursor.execute(create_query)
cursor.execute(select_query)

data = cursor.fetchone()

if (data):
    print('You are logged in')
else:
    print("Please try again")


conn.commit()

conn.close()
