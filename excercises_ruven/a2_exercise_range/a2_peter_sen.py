import sys

def myrange2(*par):
    start, finish, step = parse_params(par)
    l = []
    i = start
    while (i - finish) * step < 0:
        l.append(i)
        i += step
    return l


def myrange3(*par):
    start, finish, step = parse_params(par)

    i = start
    while (i - finish) * step < 0:
        yield i
        i += step


def parse_params(par):
    if len(par) < 1:
        raise TypeError('Should be at least 1 parameter')
    if len(par) == 1:
        start, finish, step = 0, par[0], 1
    if len(par) == 2:
        start, finish, step = par[0], par[1], 1
    if len(par) == 3:
        start, finish, step = par
    if len(par) > 3:
        raise TypeError('Should be not more than 3 parameters')
    return start, finish, step


