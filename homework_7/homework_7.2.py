# 2. Создайте класс ATM, описывающий работу банкомата. Банкомат должен
# хранить количество купюр номиналом 20, 50 и 100. Начальное количество
# купюр каждого номинала передается при создании объекта через
# __init__().
# Реализуйте метод add_money(), позволяющий добавить в банкомат
# купюры каждого номинала. Также реализуйте метод withdraw(amount)
# для снятия указанной суммы. Метод должен определить, может ли
# банкомат выдать запрошенную сумму имеющимися купюрами. Если
# операция возможна, необходимо уменьшить количество купюр в
# банкомате, вывести, сколько купюр каждого номинала было выдано, и
# вернуть True. Если указанную сумму выдать невозможно — вернуть False
# и оставить содержимое банкомата без изменений.
# Создайте объект ATM, добавьте в него несколько купюр и выполните
# несколько операций снятия денег.

class ATM:
    def __init__(self, bills_20=0, bills_50=0, bills_100=0):

        self.bills_20 = bills_20
        self.bills_50 = bills_50
        self.bills_100 = bills_100

    def add_money(self, bills_20=0, bills_50=0, bills_100=0):

        self.bills_20 += bills_20
        self.bills_50 += bills_50
        self.bills_100 += bills_100
        print(f"Добавлено: {bills_20}×20, {bills_50}×50, {bills_100}×100")

    def withdraw(self, amount: int):

        temp_20, temp_50, temp_100 = self.bills_20, self.bills_50, self.bills_100
        inserted_20 = inserted_50 = inserted_100 = 0

        # Сначала пытаемся выдать купюрами 100
        while temp_100 > 0 and amount >= 100:
            temp_100 -= 1
            inserted_100 += 1
            amount -= 100

        # Затем купюрами 50
        while temp_50 > 0 and amount >= 50:
            temp_50 -= 1
            inserted_50 += 1
            amount -= 50

        # Наконец купюрами 20
        while temp_20 > 0 and amount >= 20:
            temp_20 -= 1
            inserted_20 += 1
            amount -= 20

        # Если после всех попыток сумма не обнулилась — операция невозможна
        if amount != 0:
            print(f"Невозможно выдать сумму {amount + inserted_20 * 20 + inserted_50 * 50 + inserted_100 * 100}")
            return False

        # Если всё получилось, обновляем реальное состояние банкомата
        self.bills_20 = temp_20
        self.bills_50 = temp_50
        self.bills_100 = temp_100

        # Выводим информацию о выданных купюрах
        print(f"Выдано: {inserted_20}×20, {inserted_50}×50, {inserted_100}×100")
        return True


# Создаём объект ATM с начальным количеством купюр
atm = ATM(bills_20=10, bills_50=5, bills_100=3)

# Добавляем ещё купюр
print("\nДобавляем деньги:")
atm.add_money(bills_20=5, bills_50=3, bills_100=2)

# Выполняем операции снятия:
print("\nОперация 1: снятие 250")
success1 = atm.withdraw(250)

print("\nОперация 2: снятие 120")
success2 = atm.withdraw(120)

print("\nОперация 3: снятие 500 (невозможно)")
success3 = atm.withdraw(500)

print("\nОперация 4: снятие 80")
success4 = atm.withdraw(80)
