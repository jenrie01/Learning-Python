def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            # print('please enter a number')
            return 'please enter a number'
    except ValueError as err:
        return err
