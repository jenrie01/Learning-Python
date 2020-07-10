from random import randint
import sys

sys.argv
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

random_num = randint(num1, num2)

while True:
    try:
        print(random_num)
        user_num = int(
            input(f'Please give a number ranging from {num1} to {num2}: '))
        if num1 <= user_num <= num2:
            if random_num == user_num:
                print('You are a genius')
                break
        else:
            print(f'Please input {num1} to {num2}!')
    except ValueError as err:
        print(err)
        continue
