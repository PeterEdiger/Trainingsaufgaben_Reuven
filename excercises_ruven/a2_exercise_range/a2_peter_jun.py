
def start_stop_step(args):
    """
    :param args is a tuple of 1-3 int
    which represent (start, stop, step) like in a range() function
    :return tuple(start, stop, step)
            None, if len(args) == 0 or len(args) > 3
    """
    if len(args) == 1:
        return  0, args[0], 1

    if len(args) == 2:
        return args[0], args[1], 1

    if len(args) == 3:
        return args[0], args[1], args[2]


def myrange2(*args):
    start, stop, step = start_stop_step(args)
    range_list = []
    num = start
    # Logic for positiv negative step
    if step < 0:
        num_in_range = start > stop
    else:
        num_in_range = start < stop
    while  num_in_range:

        range_list.append(num)
        num += step
    # Logic for positiv negative step
        if step < 0:
            num_in_range = num > stop
        else:
            num_in_range = num < stop
    return(range_list)

def myrange3(*args):

    start, stop, step = start_stop_step(args)
    num = start
    if step < 0:
        num_in_range = start > stop
    else:
        num_in_range = start < stop
    while  num_in_range:

        yield num
        num += step
        if step < 0:
            num_in_range = num > stop
        else:
            num_in_range = num < stop


my_gen = myrange3(2, 10, 2)

