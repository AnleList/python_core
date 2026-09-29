# Есть два списка:
# test_cases = ["Login", "Registration", "Checkout", "Logout"]
# statuses = ["PASS", "FAIL", "PASS", "SKIP"]
# Необходимо с помощью zip() объединить название каждого тест-кейса с
# его статусом. Создайте функцию print_report(test_cases, statuses),
# которая принимает два списка и выводит отчёт в формате Login — PASS.
# После формирования отчета программа должна определить количество
# успешных и неуспешных тестов и сообщить, можно ли считать тестовый
# запуск успешным: если есть хотя бы один FAIL, запуск считается
# неуспешным.

test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

def print_report(test_cases, statuses):

    combined = zip(test_cases, statuses)

    pass_count = 0
    fail_count = 0

    print("Отчёт по тест‑кейсам:")

    for case, status in combined:
        print(f"{case} — {status}")
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1

    print(f"Всего тестов: {len(test_cases)}")
    print(f"Успешных (PASS): {pass_count}")
    print(f"Неуспешных (FAIL): {fail_count}")

    if fail_count > 0:
        print("Тестовый запуск: НЕУСПЕШНЫЙ (есть FAIL)")
    else:
        print("Тестовый запуск: УСПЕШНЫЙ (FAIL - отсутствуют)")

print_report(test_cases, statuses)
