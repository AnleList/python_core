# Пользователь одной строкой вводит результаты запуска автотестов через
# пробел, например: PASS FAIL PASS SKIP PASS FAIL. Программа должна
# преобразовать введенную строку в список, подсчитать количество тестов
# каждого типа и вывести общую статистику. Логику подсчета необходимо
# вынести в отдельную функцию get_test_statistics(results), которая
# возвращает результат в виде словаря. Дополнительно программа должна
# вывести процент успешно пройденных тестов относительно общего
# количества тестов.
# Пример вывода:
# Всего тестов: 6
# PASS: 3
# FAIL: 2
# SKIP: 1
# Успешно: 50.0%

def get_test_statistics(results):

    added_stats = {'PASS': 0, 'FAIL': 0, 'SKIP': 0}

    for status in results:
        if status == 'PASS':
            added_stats['PASS'] += 1
        elif status == 'FAIL':
            added_stats['FAIL'] += 1
        elif status == 'SKIP':
            added_stats['SKIP'] += 1

    return added_stats

input_line = input("Введите результаты тестов через пробел, пример ввода:\n>PASS FAIL SKIP\n>")
results_list = input_line.upper().split()

stats = get_test_statistics(results_list)

total_tests = stats['PASS'] + stats['FAIL'] + stats['SKIP']

if total_tests > 0:
    success_percent = (stats['PASS'] / total_tests) * 100
    print(f"Всего тестов: {total_tests}")
    print(f"PASS: {stats['PASS']}")
    print(f"FAIL: {stats['FAIL']}")
    print(f"SKIP: {stats['SKIP']}")
    print(f"Успешно: {success_percent:.1f}%")
else:
    print("Нет корректно введённых результатов")
