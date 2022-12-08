#!/usr/bin/python3
def roman_to_int(roman_string):
    rd = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    for rs in range(len(roman_string)):
        if rs + 1 != len(roman_string) and rd[roman_sring[rs]] < rd[roman_string[rs + 1]]:
            result -= rd[roman_string[rs]]
        else:
            result += rd[roman_string[rs]]
    return result
