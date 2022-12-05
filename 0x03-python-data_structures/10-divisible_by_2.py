#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_checker = []
    listlength = len(my_list)

    for num in range(listlength):
        if my_list[num] % 2 == 0:
            div_checker.append(True)
        else:
            div_checker.append(False)

    return (div_checker)
