class ID_Card:
    def __init__(self, id_number, name, address, dob):
        self.__id_number = id_number
        self.name = name
        self.address = address
        self.dob = dob
        self.__like_to_drink_soda = False

    def __set_like_to_drink_soda(self, do_you_like_to_drink_soda):
        self.__like_to_drink_soda = do_you_like_to_drink_soda

    def give_me_money_from_bank_account(self, money):
        print('You were robbed')
        return money

    def is_like_to_drink_soda(self):
        return True


id_ethan_card = ID_Card(41231232, 'Ethan Bar', 'Haifa Adam 123', ' 12 October 1993')
# print(id_ethan_card.__id_number)
print(id_ethan_card.name)
print(id_ethan_card.__id_number)
id_ethan_card.like_to_drink_soda = True
id_ethan_card2 = ID_Card(41231232, 'Ethan Bar', 'Haifa Adam 123', ' 12 October 1993')
id_ethan_card3 = ID_Card(41231232, 'Ethan Bar', 'Haifa Adam 123', ' 12 October 1993')
id_ethan_card4 = ID_Card(41231232, 'Ethan Bar', 'Haifa Adam 123', ' 12 October 1993')
id_ethan_card2.like_to_drink_soda = False
id_ethan_card3.like_to_drink_soda = True
