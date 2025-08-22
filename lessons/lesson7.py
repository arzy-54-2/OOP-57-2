import sqlite3


# A4
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (100) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
connect.commit()

# CRUD - Create Read Update Delete

def add_user(name_1, age_1, hobby_1):
    # cursor.execute(
    #     "INSERT INTO users(name, age, hobby) VALUES(?, ?, ?)",
    #     (name_1, age_1, hobby_1)
    # )
    cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name_1}", "{age_1}", "{hobby_1}")')
    connect.commit()
    print('Пользователь добавлен!!')

# add_user('Андрей', 15, "Летать")
# add_user('Ardager', 25, "Летать")
# add_user('Arzy', 26, "Летать")
# add_user('Oleg', 12, "Летать")
# add_user('Alex', 33, "Летать")




def get_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()

    for i in users:
        print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")



def update_user(name, row_id):
    # cursor.execute(
    #     'UPDATE users SET name = ? WHERE rowid = ?',
    #     (name, row_id)
    # )
    cursor.execute(f'UPDATE users SET name = "{name}" WHERE rowid = "{row_id}"')
    connect.commit()
    print('Пользователь обнавлен')

update_user("Arzy", 1)


def delete_user(row_id):
    # cursor.execute(
    #     'DELETE FROM users WHERE rowid = ?',
    #     (row_id,)
    # )

    cursor.execute(f'DELETE FROM users WHERE id = "{row_id}"')
    connect.commit()
    print('Пользоватлеь удален!')

delete_user(4)

get_users()