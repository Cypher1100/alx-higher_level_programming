#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_result_list = []
    for element in range(0, list_length):
        try:
            div_result = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            div_result = 0
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            div_result_list.append(div_result)
    return (div_result_list)
