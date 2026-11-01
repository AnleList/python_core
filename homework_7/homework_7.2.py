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

        print("\nДобавляем деньги:")
        self.bills_20 += bills_20
        self.bills_50 += bills_50
        self.bills_100 += bills_100
        print(f"Добавлено: {bills_20}×20, {bills_50}×50, {bills_100}×100")

    def withdraw(self, amount: int):

        best_combination = None

        for count_100 in range(self.bills_100, -1, -1):
            for count_50 in range(self.bills_50, -1, -1):
                for count_20 in range(self.bills_20, -1, -1):
                    total = count_100 * 100 + count_50 * 50 + count_20 * 20
                    if total == amount:
                        best_combination = (count_20, count_50, count_100)
                        break
                    elif total > amount:
                        continue
                if best_combination:
                    break
            if best_combination:
                break

        if best_combination:
            count_20, count_50, count_100 = best_combination
            self.bills_20 -= count_20
            self.bills_50 -= count_50
            self.bills_100 -= count_100

            print(f"Выдано: {count_20}×20, {count_50}×50, {count_100}×100")
            return True
        else:
            print(f"Невозможно выдать сумму {amount}")
            return False


atm = ATM(bills_20=10, bills_50=5, bills_100=3)

atm.add_money(bills_20=5, bills_50=3, bills_100=2)

sums = (120, 250, 160, 80, 1000)
for i, summ in enumerate(sums, 1):
    print(f"\nОперация {i}: снятие {summ}")
    if atm.withdraw(summ):
        print("операция выполнена")
    else:
        print("отказ")
