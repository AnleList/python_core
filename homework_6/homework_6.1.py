# Рекурсивный подсчет результатов тестов. Дан список результатов
# автотестов со статусами PASS, FAIL и SKIP. Напишите рекурсивную
# функцию, которая подсчитывает количество тестов со статусом PASS.
# Функция должна обрабатывать список с помощью рекурсии.
# Использовать циклы for и while нельзя.

test_results = ['PASS', 'FAIL', 'PASS', 'SKIP', 'PASS']


def count_pass_tests(in_def_test_results):
    # условие выхода из рекурсии:
    if not in_def_test_results:
        return 0

    if in_def_test_results[0] == 'PASS':
        return 1 + count_pass_tests(in_def_test_results[1:len(in_def_test_results)])
    else:
        return count_pass_tests(in_def_test_results[1:len(in_def_test_results)])


print(f"Количество тестов со статусом PASS: {count_pass_tests(test_results)}")
