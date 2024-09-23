from abc import ABC, abstractmethod


class MenuItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self):
        pass


class Beverage(MenuItem):
    def __init__(self, name, price, drink_volume):
        super().__init__(name, price)
        self.drink_volume = drink_volume

    def get_info(self):
        return f'{self.name} ({self.drink_volume} ml) ------- price : ${self.price}'


class MainCourse(MenuItem):
    def __init__(self, name, price, serving_size):
        super().__init__(name, price)
        self.serving_size = serving_size

    def get_info(self):
        return f'{self.name} ({self.serving_size} gram) -------- price : ${self.price}'


class Dessert(MenuItem):
    def __init__(self, name, price, number_of_calories):
        super().__init__(name, price)
        self.number_of_calories = number_of_calories

    def get_info(self):
        return f'{self.name} ({self.number_of_calories} kilocalories) ------  price : ${self.price}'


class Order(ABC):
    def __init__(self, items):
        self.items = items

    # def add_item(self, item):
    #     self.items.append(item)
    @abstractmethod
    def total_price(self):
        pass


class DineInOrder(Order):
    def __init__(self, items, table_number):
        super().__init__(items)
        self.table_number = table_number

    def total_price(self):
        total_price = 0
        if not self.items:
            return total_price
        else:
            for item in self.items:
                total_price += item.price
        return total_price


class TakeoutOrder(Order):
    def __init__(self, items, delivery_type):
        super().__init__(items)
        self.delivery_type = delivery_type

    def total_price(self):
        total_price = 0
        if not self.items:
            return total_price
        else:
            for item in self.items:
                total_price += item.price
        return total_price


def place_order(order):
    discount = 0
    print('Your orders: ')
    for item in order.items:
        print(item.get_info())

    print(f'total order price (without discount):{order.total_price()}')
    if order.total_price() >= 50:
        discount = order.total_price() * 10 / 100
        print(f'Your discount: {discount}')
    else:
        print(f'Your discount: {discount}')

    print(f'Final price payable: {order.total_price() - discount}')


water = Beverage("water", 50.99, 250)
pizza = MainCourse("pizza", 15.99, 300)
tiramisu = Dessert("Tiramisu", 5.99, 450)
o1 = DineInOrder([water, pizza, tiramisu], 29)
place_order(o1)