# def multiply_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


# print(multiply_by_2([1, 2, 3]))
my_list = [1, 2, 3]


def multiply_by_2(item):
    return item*2


print(list(map(multiply_by_2, my_list)))
print(my_list)
