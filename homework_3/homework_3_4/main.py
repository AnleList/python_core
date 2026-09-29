# Создайте второй файл main.py. Импортируйте в него созданный модуль,
# запросите у пользователя количество необходимых тестовых
# пользователей и сформируйте их список. После генерации выведите
# пользователей и статистику по статусам ACTIVE, BLOCKED и INACTIVE.

import test_data.test_data as test_data

num_users = int(input("Введите количество тестовых пользователей: "))

users = []
for each_user_num in range(num_users):
    users.append(test_data.generate_user())

print("\nСгенерированные пользователи:")
for i in range(len(users)):
    print_user = users[i]
    print(f"{i + 1}.Логин: {print_user['login']}, Возраст: {print_user['age']}, Статус: {print_user['status']}")

status_stats = {'ACTIVE': 0, 'BLOCKED': 0, 'INACTIVE': 0}
for user in users:
    status = user['status']
    if status in status_stats:
        status_stats[status] += 1

print("\nСтатистика по статусам:")
for status in status_stats:
    print(f"{status}: {status_stats[status]}")
