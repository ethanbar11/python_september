class Drink:
    def __init__(self, name, price, is_contains_sugar):
        self.name = name
        self.price = price
        self.is_contains_sugar = is_contains_sugar


class Sprite(Drink):
    def __init__(self, name, price, is_contains_sugar):
        super().__init__(name, price, is_contains_sugar)

    def shake(self):
        print('Im being shaked!')


class CocaCola(Drink):
    def __init__(self, name, price, is_contains_sugar):
        super().__init__(name, price, is_contains_sugar)

    def drink_me_cold(self):
        print('Aaaah')


drinks = {}
drinks['Coca Cola'] = CocaCola('Coca cola', 40, True)
drinks['Sprite'] = Sprite('Sprite', 20, False)


drinks = {}
