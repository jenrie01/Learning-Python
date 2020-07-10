class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)  # or use super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard('Ichi', 60, 'ichi@gmail.com')
print(wizard1.email)
