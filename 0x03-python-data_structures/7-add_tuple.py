#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lengtha = len(tuple_a)
    lengthb = len(tuple_b)

    if lengtha == 0:
        a1 = 0
        a2 = 0
    elif lengtha == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if lengthb == 0:
        b1 = 0
        b2 = 0
    elif lengthb == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    tuple_sum = (a1 + b1, a2 + b2)

    return (tuple_sum)
