# Error Handling
while True:
    try:
        age = int(input('What is your age? '))
        10/age
        #raise ValueError('hey cut it out')
    except ValueError:
        print('Please enter a number!')
    except ZeroDivisionError:
        print('Please enter a number higher than 0!')
    except:
        print('unknown error')
    else:
        print('Thank you !')
        break
    finally:
        print('Ok, I am finally done!')
# def sum(num1, num2):
#     try:
#         return num1/num2
#     # except TypeError as err:
#     #     print(f'Please enter numbers {err}')
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)


# print(sum(1, 0))
