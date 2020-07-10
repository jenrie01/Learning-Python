my_list = [1, 2, 3]
your_list = [5, 6, 7]
their_list = [300, 450, 600]


def multiply_by_2(item):
    return item*2


def odd_only(item):
    return item % 2 != 0


print(list(zip(my_list, your_list, their_list)))
print(my_list)
