# patterns/safer_sum.py
def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [int(first) | float(first), *rest]:
            return first + sum_list(rest)
        case _: 
            raise ValueError("Can only sum lists of numbers")
