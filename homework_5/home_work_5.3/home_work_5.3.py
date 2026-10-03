# 3. Напишите функцию, которая принимает количество повторных запусков
# теста и значение таймаута. Количество повторных запусков должно
# находиться в диапазоне от 0 до 5, а таймаут должен быть положительным
# числом. Если переданные значения не соответствуют этим требованиям,
# самостоятельно создайте исключение ValueError с помощью raise и
# добавьте понятное описание причины ошибки. Вызов функции
# необходимо поместить в try/except и корректно обработать созданные
# исключения. Проверьте работу программы минимум на трёх наборах
# данных: корректные значения, отрицательный таймаут и слишком
# большое количество повторных запусков
from turtledemo.penrose import start


def configure_test_retries(restarts, timeout_value):

    # Проверка количества повторных запусков
    if not isinstance(restarts, int):
        raise ValueError("Количество повторных запусков должно быть целым числом.")
    if restarts < 0 or restarts > 5:
        raise ValueError(f"Количество повторных запусков ({restarts}) должно быть в диапазоне от 0 до 5.")

    # Проверка таймаута
    if timeout_value <= 0:
        raise ValueError(f"Таймаут ({timeout_value}) должен быть положительным числом.")

    return f"Настройки: повторные запуски = {restarts}, таймаут = {timeout_value}."

test_cases = [
    # корректные значения
    (3, 10),
    # отрицательный таймаут
    (2, -5),
    # слишком большое количество повторных запусков
    (10, 30)
]

for i, test in enumerate(test_cases, start=1):
    retries = test[0]
    timeout = test[1]
    print(f"Тест #{i}: retries={retries}, timeout={timeout}")
    try:
        test_result = configure_test_retries(retries, timeout)
        print(f"Результат: {test_result}")
    except ValueError as e:
        print(f"Ошибка: {e}")
