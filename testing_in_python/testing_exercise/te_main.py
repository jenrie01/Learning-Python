from random import randint
import sys
# generate a number 1~10


def guessing_game(answer, guess=2):
    try:
        if 0 < int(guess) < 11:
            if guess == answer:
                print('you are a genius!')
                return True
        else:
            return 'hey bozo, I said 1~10'
    except ValueError as err:
        return err


if __name__ == "__main__":
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if (guessing_game(answer, guess)):
                break
        except ValueError as err:
            print(err)
            continue


# def guessing_game(guess=1):
#     try:
#         # guess = int(input('guess a number 1~10:  '))
#         if 0 < int(guess) < 11:
#             if guess == answer:
#                 # print('you are a genius!')
#                 return 'you are a genius!'
#                 # break
#         else:
#             # print('hey bozo, I said 1~10')
#             return 'hey bozo, I said 1~10'
#     except ValueError as err:
#         # print('please enter a number')
#         return err
#         # continue
