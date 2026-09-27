# 1. Дан список результатов автотестов. Для каждого теста известны его
# название, статус выполнения (PASS, FAIL или SKIP) и время выполнения.
# Напишите программу, которая с помощью filter() получает все
# упавшие тесты, с помощью map() формирует список их названий, а с
# помощью reduce() рассчитывает общее время выполнения всех тестов.
# Дополнительно с помощью генератор списка сформируйте список
# названий успешно пройденных тестов. В результате программа должна
# вывести количество тестов каждого статуса, список названий упавших
# тестов, список успешно пройденных тестов и общее время выполнения
# всех тестов

from functools import reduce

test_results = [
    {'name': 'test_login', 'status': 'PASS', 'time': 2.5},
    {'name': 'test_registration', 'status': 'FAIL', 'time': 3.1},
    {'name': 'test_profile', 'status': 'PASS', 'time': 1.8},
    {'name': 'test_payment', 'status': 'FAIL', 'time': 4.2},
    {'name': 'test_api', 'status': 'SKIP', 'time': 0.5},
    {'name': 'test_security', 'status': 'PASS', 'time': 5.0},
    {'name': 'test_performance', 'status': 'SKIP', 'time': 10.0}
]

# Получаем упавшие тесты (FAIL) с помощью filter()
failed_tests = list(filter(lambda test: test['status'] == 'FAIL', test_results))


# Формируем список названий упавших тестов с помощью map()
failed_test_names = list(map(lambda test: test['name'], failed_tests))

# Рассчитываем общее время выполнения всех тестов с помощью reduce()
total_time = reduce(lambda acc, test: acc + test['time'], test_results, 0.0)

# Формируем список успешно пройденных тестов (PASS) с помощью генератора списка
passed_test_names = [test['name'] for test in test_results if test['status'] == 'PASS']

# Подсчитываем количество тестов каждого статуса
status_counts = {}
for test in test_results:
    status = test['status']
    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1

# Выводим результаты
print("Количество тестов по статусам:")
for status, count in status_counts.items():
    print(f"  {status}: {count}")

print(f"\nУпавшие тесты ({len(failed_test_names)}):")
for name in failed_test_names:
    print(f"  - {name}")

print(f"\nУспешно пройденные тесты ({len(passed_test_names)}):")
for name in passed_test_names:
    print(f"  - {name}")

print(f"\nОбщее время выполнения всех тестов: {total_time:.2f} секунд")
