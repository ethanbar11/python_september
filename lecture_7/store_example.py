# class <class_name>
class Store:
    def __init__(self, name, rent, address):
        # self.color = color
        self.name = name
        self.items = {}
        self.item_weights = {}
        self.rent = rent
        self.address = address

    def add_item(self, item_name, item_weight, amount):
        self.items[item_name] = amount
        self.item_weights[item_name] = item_weight

    def remove_item(self, item_name):
        del self.items[item_name]

    def print_items(self):
        print('Color is:', self.color)
        for item in self.items.keys():
            print('Item name:', item, 'Amount :', self.items[item])


class Cigarette:
    def __init__(self, company_name, cigarette_name):
        self.company_name = company_name
        self.cigarrete_name = cigarette_name


store_ethan = Store('Green')
store_ethan.add_item('Carrot', 50)
store_ethan.add_item('Pineapple', 100)
store_ethan.add_item('Oven', 10)
store_ethan.remove_item('Oven')
store_ethan.print_items()
print()
store_baruch = Store('Red')
store_baruch.add_item('Headphones', 50)
store_baruch.add_item('Mouse', 10)
store_baruch.print_items()
