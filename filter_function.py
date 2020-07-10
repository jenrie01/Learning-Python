my_list = [1, 2, 3]


def multiply_by_2(item):
    return item*2


def odd_only(item):
    return item % 2 != 0


print(list(filter(odd_only, my_list)))
print(my_list)
