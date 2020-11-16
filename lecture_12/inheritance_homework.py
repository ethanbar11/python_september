class System:
    def __init__(self):
        self.signed_up_users = {}
        self.signed_in_users = {}

    def sign_up(self, user, password):
        if not user in self.signed_up_users:
            self.signed_up_users[user] = password
        else:
            raise SignException('{}  is an already registered user!'.format(user))
            # print()

    def sign_in(self, user, password):
        if user in self.signed_up_users and user not in self.signed_in_users:
            if self.signed_up_users[user] == password:
                self.signed_in_users[user] = True
                return "User signed in!"
            else:
                return "Password incorrect!"

    def print_all_connected_users(self):
        print(self.signed_in_users.keys())

    def sign_out(self, user):
        if user in self.signed_in_users:
            del self.signed_in_users[user]
            return "User signed out"
        else:
            return "Operation incorrect."


class SignException(Exception):
    pass


if __name__ == '__main__':
    system=System()
    system.sign_up('Ethan','1234')
    system.sign_up('Ethan','1234')
    system.sign_in('Ethan','1234')
    system.print_all_connected_users()
    # system.sign_up('Ethan','1234')