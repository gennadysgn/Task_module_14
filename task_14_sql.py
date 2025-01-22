import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполнение 10-ю записями:
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", f"{1000}"))

# Обновление balance у каждой 2-ой записи начиная с 1-ой на 500:
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 != 0")

# Удаление каждой 3-й записи в таблице начиная с 1-ой:
i = 1
while i < 11:
    cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))
    i += 3

# Выборка всех записей при помощи fetchall(), где возраст не равен 60 и вывод их в консоль без id:
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя:{user[0]} | Почта:{user[1]} | Возраст:{user[2]} | Баланс:{user[3]}")

# Консоль:
# Имя:User2 | Почта:example2@gmail.com | Возраст:20 | Баланс:1000
# Имя:User3 | Почта:example3@gmail.com | Возраст:30 | Баланс:500
# Имя:User5 | Почта:example5@gmail.com | Возраст:50 | Баланс:500
# Имя:User8 | Почта:example8@gmail.com | Возраст:80 | Баланс:1000
# Имя:User9 | Почта:example9@gmail.com | Возраст:90 | Баланс:500

# Второй этап:

# Удаление из базы данных not_telegram.db запись с id = 6:
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчет общего количества записей:
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print(total_users)

# Консоль:
# 5

# Подсчет суммы всех балансов:
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances)

# Консоль:
# 3500

# Вывод в консоль средний баланс всех пользователей:
print(all_balances / total_users)

connection.commit()
connection.close()

# Консоль:
# 700.0