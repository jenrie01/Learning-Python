# list, set, dictionary
# my_list = [param for param in iterable]
# doing this
# my_list = []
# for char in 'hello':
#     my_list.append(char)
# is the same as doing this
my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num * 2 for num in range(0, 100)}
my_set4 = {num ** 2 for num in range(0, 100)}
my_set5 = {num ** 2 for num in range(0, 100) if num % 2 == 0}
# print(my_set)
# print(my_set2)
# print(my_set3)
# print(my_set4)
# print(my_set5)
