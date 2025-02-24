import sqlite3

# Подключаемся к базе данных (создаст файл, если его нет)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Создаем таблицу
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
""")

# Добавляем данные
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Алексей", 28))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Иван", 18))

# Фиксируем изменения
conn.commit()

# Выбираем данные
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Закрываем соединение
conn.close()
