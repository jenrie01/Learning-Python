class PlayerCharacter:  # blueprint
    # Class Object Attribute - static
    membership = True

    def __init__(self, name, age):  # object
        '''
        Function containing its attributes.\n
        self refers to PlayerCharacter
        '''
        if(self.membership):
            self.name = name  # attribute - dynamic
            self.age = age  # attribute - dynamic

    def run(self):  # object
        '''
        Function containing run.
        '''
        print('run')
        return 'running'

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        # return num1 + num2
        return cls('Teddy', num1 + num2)
        # can also be used like this to instantiate a new object

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 30)  # instantiate
player2 = PlayerCharacter('Tom', 25)  # instantiate
player2.attack = 50
player3 = PlayerCharacter.adding_things(3, 5)

print(f'Name: {player1.name} \n Age: {player1.age} \n Status: {player1.run()} \n')
print(f'Name: {player2.name} \n Age: {player2.age} \n Attack: {player2.attack}')
print(player1.shout())
print(player2.shout())
# print(PlayerCharacter.adding_things(3, 5))
print(player3.age)
