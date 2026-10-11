# Домашнее задание
# Разработать программу для работы с цветами и букетами, используя
# принципы объектно-ориентированного программирования.
# Необходимо:
# ● Определить иерархию классов цветов и реализовать несколько
# различных видов цветов.
# ● Для каждого цветка предусмотреть основные характеристики: название,
# стоимость и время жизни.
# ● Реализовать возможность собирать букет из разных цветов.
# ● Добавить в букет возможность использования аксессуаров и учитывать
# их стоимость при расчете общей стоимости букета.
# ● Реализовать метод для определения общей стоимости букета.
# ● Определить время увядания букета на основании среднего времени
# жизни всех цветов, входящих в него.
# ● Реализовать возможность сортировки цветов в букете по стоимости.
# ● Реализовать возможность проверить, присутствует ли определённый
# цветок в букете.
# При выполнении задания использовать классы, наследование, композицию и
# методы объектов.


def format_cents(cents):
    rub = cents // 100
    cop = cents % 100
    return f"{rub} руб. {cop:02d} коп."


class Flower:
    def __init__(self, name, price_cents, life_days):
        self.name = name
        self.price_cents = price_cents
        self.life_days = life_days

    def __repr__(self):
        return f"{self.name} ({format_cents(self.price_cents)}, {self.life_days} дн.)"


class Rose(Flower):
    def __init__(self, color, price_cents, life_days=7):
        super().__init__(name=f"Роза ({color})", price_cents=price_cents, life_days=life_days)
        self.color = color


class Tulip(Flower):
    def __init__(self, color, price_cents, life_days=5):
        super().__init__(name=f"Тюльпан ({color})", price_cents=price_cents, life_days=life_days)
        self.color = color


class Orchid(Flower):
    def __init__(self, variety, price_cents, life_days=14):
        super().__init__(name=f"Орхидея ({variety})", price_cents=price_cents, life_days=life_days)
        self.variety = variety


class Accessory:
    def __init__(self, name, price_cents):
        self.name = name
        self.price_cents = price_cents

    def __repr__(self):
        return f"{self.name} (+{format_cents(self.price_cents)})"


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def total_price_str(self):
        total_flowers_price = sum(flower.price_cents for flower in self.flowers)
        total_accessories_price = sum(accessory.price_cents for accessory in self.accessories)
        return format_cents(total_flowers_price + total_accessories_price)

    def wilting_time_days(self):
        if not self.flowers:
            return None
        total_life = sum(flower.life_days for flower in self.flowers)
        return total_life / len(self.flowers)

    def sort_by_price(self):
        return sorted(self.flowers, key=lambda flower: flower.price_cents)

    def has_flower_by_name(self, name):
        return any(flower.name == name for flower in self.flowers)

    def describe(self):
        lines = ["Состав букета:"]
        if self.flowers:
            for flower in self.flowers:
                lines.append(f"  - {flower}")
        else:
            lines.append("  (нет цветов)")

        if self.accessories:
            for accessory in self.accessories:
                lines.append(f"  + {accessory}")

        lines.append(f"Общая стоимость: {self.total_price_str()}")

        wilting = self.wilting_time_days()
        if wilting is not None:
            lines.append(f"Ожидаемое время увядания букета: {wilting} дн.")
        else:
            lines.append("Ожидаемое время увядания букета не определено - нет цветов")

        return "\n".join(lines)


# Демонстрация
red_rose = Rose(color="красная", price_cents=15000, life_days=7)
white_rose = Rose(color="белая", price_cents=16050, life_days=8)
yellow_tulip = Tulip(color="жёлтый", price_cents=9030, life_days=5)
purple_orchid = Orchid(variety="Фаленопсис", price_cents=35099, life_days=14)

ribbon = Accessory(name="Атласная лента", price_cents=7000)
wrap = Accessory(name="Упаковочная плёнка", price_cents=5050)

bouquet = Bouquet()
bouquet.add_flower(red_rose)
bouquet.add_flower(white_rose)
bouquet.add_flower(yellow_tulip)
bouquet.add_flower(purple_orchid)
bouquet.add_accessory(ribbon)
bouquet.add_accessory(wrap)

print(bouquet.describe())
print()

sorted_flowers = bouquet.sort_by_price()
print("Цветы, отсортированные по стоимости:")
for f in sorted_flowers:
    print(f"  {f}")
print()

check_name = "Роза (красная)"
if bouquet.has_flower_by_name(check_name):
    print(f"{check_name} есть в букете.")
else:
    print(f"{check_name} нет в букете.")
