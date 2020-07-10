try:
    with open('filepaths/fp_example.txt') as my_file:
        print(my_file.read())
except FileNotFoundError as err1:
    print('File does not exist')
except IOError as err2:
    print('IO error')

# pathlib - must read some other time
