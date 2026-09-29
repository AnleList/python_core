# Результаты автотестов. Пользователь вводит количество выполненных
# автотестов, а затем по очереди результат каждого теста: PASS, FAIL или
# SKIP. Программа должна подсчитать количество тестов с каждым
# статусом и вывести итоговую статистику. Если присутствует хотя бы один
# FAIL, необходимо сообщить о наличии упавших тестов; если FAIL
# отсутствуют - сообщить об успешном прохождении выполненных тестов.
# Любой неизвестный статус необходимо пропустить и не учитывать в
# статистике.

count_pass = 0
count_fail = 0
count_skip = 0

total_tests = int(input("Введите количество выполненных автотестов: "))

print(f"Введите результат каждого из {total_tests} тестов (PASS, FAIL или SKIP):")

for i in range(total_tests):
    status = input(f"Тест {i + 1}: ").strip().upper()

    if status == "PASS":
        count_pass += 1
    elif status == "FAIL":
        count_fail += 1
    elif status == "SKIP":
        count_skip += 1

print("\n--- Итоговая статистика ---")
print(f"PASS: {count_pass}")
print(f"FAIL: {count_fail}")
print(f"SKIP: {count_skip}")

if count_fail > 0:
    print("\nВнимание: обнаружены упавшие (FAIL) тесты!")
else:
    print("\nТесты успешно пройдены (FAIL тесты отсутствуют).")
