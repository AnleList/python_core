# Дан список тестов:
# tests = [
# "test_login",
# "test_logout",
# "test_registration",
# "test_profile",
# "test_payment",
# "test_search"
# ]Пользователь вводит количество тестов, которые необходимо запустить.
# Программа должна случайным образом выбрать указанное количество
# уникальных тестов из списка и каждому выбранному тесту случайно
# назначить статус PASS, FAIL или SKIP. Результаты необходимо объединить
# и вывести в виде отчёта. Если пользователь запросил больше тестов, чем
# существует в списке, программа должна вывести сообщение об ошибке.

import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]

STATUSES = ["PASS", "FAIL", "SKIP"]

num_tests = int(input("Введите количество тестов, которые необходимо запустить: "))

if num_tests > len(tests):
    print(f"Ошибка: невозможно запустить {num_tests} тестов — в списке всего {len(tests)} тестов.")
else:
    selected_tests = random.sample(tests, num_tests)

    report = []
    for test in selected_tests:
        status = random.choice(STATUSES)
        report.append((test, status))

    print("\nОтчёт по запуску тестов:")
    for test, status in report:
        print(f"{test} — {status}")

    pass_count = 0
    fail_count = 0
    skip_count = 0

    for test_name, status in report:
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1
        else:
            skip_count += 1

    print(f"\nВсего запущено тестов: {len(report)}")
    print(f"PASS: {pass_count}")
    print(f"FAIL: {fail_count}")
    print(f"SKIP: {skip_count}")
