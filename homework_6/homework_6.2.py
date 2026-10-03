# 2. Замыкание для проверки времени выполнения. Напишите функцию
# create_time_checker(max_time), которая возвращает вложенную
# функцию для проверки времени выполнения теста. Вложенная функция
# принимает фактическое время выполнения и сообщает, превышен
# установленный лимит или нет. Создайте два независимых замыкания с
# разными значениями max_time и продемонстрируйте их работу.

# создадим список времени выполнения тестов
test_times = [0.3, 0.7, 2.5]


def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time > max_time:
            return f"Фактическое время: {actual_time} сек.\n - установленный лимит - превышен!"
        else:
            return f"Фактическое время: {actual_time}\n - в пределах лимита."

    return check_time


def demonstration(checkers_dict, dem_test_times):
    for limit, checker in checkers_dict.items():
        print(f"\nДемонстрируем работу с лимитом {limit}:")
        for test_time in dem_test_times:
            print(f"{checker(test_time)}")


# Зададим лимиты max_time для двух независимых замыканий
max_time_limits = (0.5, 2.0)
# Создадим наши замыкания:
checkers = {limit: create_time_checker(limit) for limit in max_time_limits}

# Демострация работы независимых замыканий:
demonstration(checkers, test_times)
