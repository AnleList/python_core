# Создайте JSON-файл с тестовыми пользователями для проверки
# авторизации. Для каждого пользователя должны храниться логин, пароль
# и ожидаемый результат авторизации. Напишите программу, которая
# открывает JSON-файл, загружает данные и выводит информацию о
# каждом тестовом пользователе. Программа должна корректно
# обрабатывать ситуации, когда файл не существует, содержимое файла
# невозможно прочитать как JSON или у пользователя отсутствует
# обязательное поле. Для обработки ошибок используйте try/except,
# соответствующие типы исключений и получение информации об ошибке
# через as e.

import json
import os

filename = "test_users.json"

try:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не найден.")

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    print(f"Загружено {len(data)} тестовых пользователей:\n")

    for i, user in enumerate(data, start=1):
        try:
            if 'login' not in user:
                raise KeyError("Отсутствует поле 'login'")
            if 'password' not in user:
                raise KeyError("Отсутствует поле 'password'")
            if 'expected_result' not in user:
                raise KeyError("Отсутствует поле 'expected_result'")

            print(f"Пользователь #{i}:")
            print(f"  Логин: {user['login']}")
            print(f"  Пароль: {user['password']}")
            print(f"  Ожидаемый результат: {user['expected_result']}")
            print("-" * 30)

        except KeyError as e:
            print(f"Ошибка в данных пользователя #{i}: {e}")

except FileNotFoundError as e:
    print(f"Ошибка: {e}")
except json.JSONDecodeError as e:
    print(f"Ошибка чтения JSON: файл '{filename}' содержит некорректные данные. Подробности: {e}")
except Exception as e:
    print(f"Неожиданная ошибка: {e}")
