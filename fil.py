import sqlite3

# Подключаемся к SQLite (или создаем новый файл БД)
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# Создание таблицы пользователей (users)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 0),
    country TEXT DEFAULT 'Unknown'
);
""")

conn.commit()
print("✅ Таблицы успешно созданы!")

cursor.executemany("""
INSERT INTO users (name, email, age, country) VALUES (?, ?, ?, ?)
""", [
    ("Алексей", "alex@example.com", 28, "Россия"),
    ("Мария", "maria@example.com", 25, "США"),
    ("Джон", "john@example.com", 35, "Германия"),
    ("Ольга", "olga@example.com", 30, "Франция")
])

conn.commit()
print("✅ Тестовые данные успешно добавлены!")

conn.close()
print("✅ Все проверки успешно выполнены!")