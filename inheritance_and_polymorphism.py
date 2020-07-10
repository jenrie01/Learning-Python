class User():  # parent class
    def sign_in(self):
        print('logged in')

    def attack(self):  # for polymorphism example
        print('do nothing')


class Wizard(User):  # children class or sub class
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'Attacking with power of {self.power}')


class Archer(User):  # children class or sub class
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left - {self.arrows}')


wizard1 = Wizard('Psykeeper', 3000)
archer1 = Archer('Bow Jester', 5932)
wizard1.attack()
archer1.attack()


def player_attack(char):
    char.attack()


'''
Example of Polymorphism
'''

player_attack(wizard1)
player_attack(archer1)

# or
# for char in [wizard1, archer1]:
#     char.attack()
