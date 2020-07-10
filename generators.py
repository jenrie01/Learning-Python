# range(100)
# list(range(100))


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result


# my_list = make_list(100)
# print(my_list)

# iterable
# iterate
# generators

def generator_function(num):
    for i in range(num):
        yield i


# g = generator_function(10)
# print(next(g))
# print(next(g))
# print(next(g))
for item in generator_function(1000):
    print(item)
