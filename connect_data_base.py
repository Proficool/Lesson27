
import psycopg2

# Данные подключения
HOST = "2.tcp.eu.ngrok.io"
PORT = 16326
DATABASE = "Lesson17"
USER = "slalov"
PASSWORD = "slalov"

try:
    # Подключаемся к базе данных
    conn = psycopg2.connect(
        dbname=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

    # Создаём курсор для выполнения SQL-запросов
    cursor = conn.cursor()
    print('aaa')

    # Выполним тестовый запрос
    #cursor.execute("SELECT * from users;")
    #cursor.execute("SELECT users.name, orders.product, orders.price from users INNER JOIN orders ON users.id = orders.user_id;")
    cursor.execute("SELECT users.name, orders.product, orders.price from users LEFT JOIN orders ON users.id = orders.user_id WHERE orders.id IS NULL;")

    # Получаем результат
    db_version = cursor.fetchall()
    print(f"Всем юзеры {db_version}")

    # Закрываем соединение
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Ошибка подключения: {e}")