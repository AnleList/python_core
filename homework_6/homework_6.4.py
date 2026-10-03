# 4. Декоратор повторного запуска. Напишите декоратор с параметром
# retry(count), который повторно запускает декорируемую функцию
# указанное количество раз, пока функция не вернет True. Перед каждой
# попыткой необходимо выводить её номер. Если функция вернула True,
# дальнейшие попытки выполнять не нужно. Декоратор должен
# поддерживать передачу позиционных и именованных аргументов через
# *args и **kwargs.

import functools
import random


def retry(count):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка {attempt}/{count}")
                result = func(*args, **kwargs)

                if result is True:
                    print(f"Успех на попытке {attempt}!")
                    return True
            print("Все попытки исчерпаны.")
            return False
        return wrapper

    return decorator

@retry(4)
def check_connection(rate_limit = 5):
    fact_rate = random.randint(1, int(rate_limit*1.8))
    print(f"факт время соединения: {fact_rate}")
    if fact_rate < 5:
        print(" - соединение установлено за установленное время!")
        return True
    else:
        print(" - превышено время ожедания соединения.")
        return False


check_connection()