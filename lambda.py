from functools import reduce
my_list = [1, 2, 3]

# instead of doing this

# def multiply_by_2(item):
#     return item*2

#lambda param: action(param)

# def odd_only(item):
#     return item % 2 != 0


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2, my_list)))
# filter function only return value = true so i can remove the != 0 and still get the same output
print(reduce(lambda acc, item: acc+item, my_list))
print(my_list)
