#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            else:
               final_result += (a ** b) / num
        except Exception:
            final_result = b + a
            break
    return (final_result)
