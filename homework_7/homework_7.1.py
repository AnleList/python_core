# 1. Создайте класс CreditCard, описывающий кредитную карту. При
# создании объекта необходимо передавать номер счёта и начальный
# баланс карты. Реализуйте метод deposit(amount), который пополняет
# баланс на указанную сумму, метод withdraw(amount), который снимает
# указанную сумму, и метод show_info(), который выводит номер счёта и
# текущий баланс.
# Создайте три объекта класса CreditCard с разными номерами счетов и
# начальными балансами. Пополните баланс первой и второй карты, а с
# третьей карты снимите некоторую сумму. После выполнения операций
# выведите информацию о состоянии всех трёх карт.


import random

max_account_number = 99999999999999999999
max_card_number = 9999999999999999
used_account_numbers = []
used_card_numbers = []


def generate_unique_account_number():
    while used_account_numbers.__len__() < max_account_number:
        number = f"{random.randint(0, max_account_number):020d}"
        if number not in used_account_numbers:
            used_account_numbers.append(number)
            return number
    else:
        print(f"no more account numbers")
        return f"no more account numbers"


def generate_unique_card_number():
    while used_card_numbers.__len__() < max_card_number:
        number = f"{random.randint(0, max_card_number):016d}"
        if number not in used_card_numbers:
            used_card_numbers.append(number)
            return number
    else:
        print(f"no more card numbers")
        return f"no more card numbers"


class CreditCard:
    def __init__(self, account_number, initial_balance):

        self.account_number = account_number
        self.balance = initial_balance
        self.card_number = generate_unique_card_number()

    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение на {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств. Баланс: {self.balance}, запрашиваемая сумма: {amount}")
        else:
            self.balance -= amount
            print(f"Снятие {amount}. Новый баланс: {self.balance}")

    def show_info(self):
        print(f"Карта номер: {self.card_number} привязана к счёту: {self.account_number}. Баланс карты: {self.balance}")


# Создадим 3 кредитные карты с разными номерами счетов и начальными балансами:
cards = [CreditCard(generate_unique_account_number(), random.randint(1, 1000000)) for i in range(3)]
card1, card2, card3 = cards

# Выполняем операции
print("Выполняем операции:")
card1.deposit(500)  # Пополняем первую карту
card2.deposit(300)  # Пополняем вторую карту
card3.withdraw(800)  # Снимаем с третьей карты

# Выводим информацию о состоянии всех карт
print("\nСостояние всех карт:")
card1.show_info()
card2.show_info()
card3.show_info()
