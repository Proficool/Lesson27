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

# Получаем id добавленного пользователя по имени
test_user_id = cursor.lastrowid

# Проверяем, что пользователь добавлен
cursor.execute("SELECT * FROM users WHERE id = ?", (test_user_id,))
user = cursor.fetchone()
expected_user = (test_user_id,) + test_user
assert user == expected_user, f"Ошибка: данные в БД не совпадают! Ожидалось {expected_user}, получено {user}"
print("Данные добавлены корректно:", user)

# Удаляем пользователя после теста
cursor.execute("DELETE FROM users WHERE id = ?", (test_user_id,))
conn.commit()

# Проверяем, что пользователь удален
cursor.execute("SELECT * FROM users WHERE id = ?", (test_user_id,))
assert cursor.fetchone() is None, "Ошибка: Пользователь не удален!"
print("Пользователь удален.")

# Закрываем соединение
conn.close()
