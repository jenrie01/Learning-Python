# list, set, dictionary
# my_list = [param for param in iterable]
# doing this
# my_list = []
# for char in 'hello':
#     my_list.append(char)
# is the same as doing this
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num * 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100)]
my_list5 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)
print(my_list5)
