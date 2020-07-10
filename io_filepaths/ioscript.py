# Working With Files In Python
# my_file = open('iotest.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readlines())

# my_file.close()

# Read, Write, Append
# default mode='r' to read
# mode='r+' to read and write
# mode='w' to write (overwrite or create if it's not existing)
# mode='a' to append
with open('try.txt', mode='w') as my_file:
    # text = my_file.write('hey it\'s me!')
    text = my_file.write('trial')
    print(text)
    # print(my_file.readlines())
