#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_count = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            int_count += 1
        except (ValueError, IndexError, TypeError):
            pass
    print()
    return (int_count)