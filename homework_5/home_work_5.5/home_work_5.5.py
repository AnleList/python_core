# 5. Создайте программу для формирования отчёта по результатам
# автоматизированного тестирования. Исходные данные программа
# должна получать из JSON-файла, в котором для каждого теста указаны
# название, статус и время выполнения. Программа должна определить
# общее количество тестов, количество тестов со статусами PASS, FAIL и
# SKIP, сформировать список упавших тестов, определить самый
# длительный тест и рассчитать суммарное время выполнения. При
# обработке данных необходимо использовать минимум один генератор
# списка, lambda, filter() и reduce(). Работу с файлом и входными
# данными необходимо защитить с помощью try/except: программа
# должна корректно обрабатывать отсутствие файла, некорректный JSON и
# неправильную структуру тестовых данных. Сформированный итоговый
# отчёт необходимо сохранить в отдельный JSON-файл.

import json
from functools import reduce


def generate_test_report(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as opened_input:
            data = json.load(opened_input)

        if not isinstance(data, list):
            raise ValueError("JSON должен содержать список тестов")

        valid_tests = list(filter(
            lambda test: all(key in test for key in ['name', 'status', 'duration']),
            data
        ))

        if len(valid_tests) != len(data):
            print("Предупреждение: некоторые тесты имеют некорректную структуру и будут пропущены")

        total_tests = len(valid_tests)

        def status_count(status):
            return len([t for t in valid_tests if t['status'] == f'{status}'])

        pass_count = status_count('PASS')
        fail_count = status_count('FAIL')
        skip_count = status_count('SKIP')
        failed_tests = [t for t in valid_tests if t['status'] == 'FAIL']

        longest_test = max(valid_tests, key=lambda t: t['duration']) if valid_tests else None

        durations = [test['duration'] for test in valid_tests if isinstance(test, dict) and 'duration' in test]
        total_duration = reduce(lambda acc, duration: acc + duration, durations, 0)

        report = {
            "total_tests": total_tests,
            "pass_count": pass_count,
            "fail_count": fail_count,
            "skip_count": skip_count,
            "failed_tests": failed_tests,
            "longest_test": {
                "name": longest_test['name'] if longest_test else None,
                "duration": longest_test['duration'] if longest_test else 0
            },
            "total_duration": total_duration
        }

        with open(output_file, 'w', encoding='utf-8') as opened_output:
            json.dump(report, opened_output, indent=4)

        print(f"Отчёт успешно создан и сохранён в {output_file}")
        return report

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка: Некорректный JSON в файле. {e}")
    except ValueError as e:
        print(f"Ошибка в структуре данных: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")


generate_test_report("tests_input.json", "test_report.json")
