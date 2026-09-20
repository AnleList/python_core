# Запуск тестов для пользователей. Напишите программу, которая
# последовательно запускает тестирование для пользователей с номерами
# от 1 до 20. Пользователей с номерами 5, 10 и 15 необходимо пропустить и
# продолжить выполнение программы. После достижения пользователя с
# номером 18 выполнение цикла необходимо полностью прекратить.

start_user_number = 1
max_user_number = 20
all_users = list(range(start_user_number, max_user_number + 1))
skip_users = (5, 10, 15)
stop_at_user = 18

print("Запуск тестов для пользователей...")
print(f"всего пользователей: {len(all_users)}")

for user_number in all_users:
    if user_number in skip_users:
        print(f"Пользователь {user_number}: пропуск...")
        continue
    if user_number == stop_at_user:
        print(f"Пользователь {user_number}: выполнение цикла полностью прекратить.")
        break
    print(f"Пользователь {user_number}: запуск тестирования...")
