# 3. Декоратор для логирования автотестов. Напишите декоратор log_test,
# который перед запуском тестовой функции выводит её имя, после
# выполнения сообщает о завершении и выводит полученный результат.
# Декоратор должен поддерживать функции с произвольным количеством
# позиционных и именованных аргументов с помощью *args и **kwargs.
# Используйте functools.wraps(), чтобы сохранить метаданные исходной
# функции.


import functools

def log_test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Тест {func.__name__} завершён. Результат: {result}\n")
        return result
    return wrapper


@log_test
def add_numbers(a, b):
    return a + b

@log_test
def multiply_and_subtract(x, y, subtract=0):
    return x * y - subtract

@log_test
def simple_test():
    return "Успех!"

# Тестируем декоратор:
add_numbers(5, 3)
multiply_and_subtract(4, 7, subtract=10)
simple_test()
