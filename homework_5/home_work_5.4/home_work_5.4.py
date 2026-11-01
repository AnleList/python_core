# 4. Создайте собственное исключение InvalidTestStatusError,
# наследуемое от Exception. Напишите функцию, которая принимает статус
# теста и проверяет его значение. Допустимыми считаются только PASS,
# FAIL и SKIP. Если передан любой другой статус, функция должна с
# помощью raise создать InvalidTestStatusError и передать в него
# сообщение с некорректным значением. В основной программе
# обработайте это исключение через try/except и выведите понятное
# сообщение пользователю. Проверьте программу как с корректными, так и
# с некорректными статусами.

class InvalidTestStatusError(Exception):
    pass


def validate_test_status(verified_status):
    valid_statuses = {'PASS', 'FAIL', 'SKIP'}

    if verified_status not in valid_statuses:
        raise InvalidTestStatusError(f"Недопустимый статус теста: '{verified_status}'. Допустимые статусы: PASS, FAIL, SKIP.")
    else:
        print(f"Статус теста '{verified_status}' является допустимым.")



test_statuses = ['PASS', 'FAIL', 'SKIP', 'ERROR', 'RUNNING', 'COMPLETED']

for status in test_statuses:
    try:
        validate_test_status(status)
    except InvalidTestStatusError as e:
        print(f"Ошибка: {e}")
