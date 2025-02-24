import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Вывод всех пользователей
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Текущие пользователи в базе данных:")
for row in rows:
    print(row)


# Добавляем нового пользователя
test_user = ("Виталий", "vit@example.com", 51, "Беларусь")
cursor.execute("INSERT INTO users (name, email, age, country) VALUES (?, ?, ?, ?)", test_user)
conn.commit()

# Проверяем, что пользователь добавлен
cursor.execute("SELECT * FROM users WHERE email = ?", (test_user[1],))
user = cursor.fetchone()
assert user, "Ошибка: Пользователь не добавлен!"
print("Тестовый пользователь:", user)

# Удаляем пользователя после теста
cursor.execute("DELETE FROM users WHERE email = ?", (test_user[1],))
conn.commit()

# Проверяем, что пользователь удален
cursor.execute("SELECT * FROM users WHERE email = ?", (test_user[1],))
assert cursor.fetchone() is None, "Ошибка: Пользователь не удален!"
print("Пользователь удален.")

# Закрываем соединение
conn.close()