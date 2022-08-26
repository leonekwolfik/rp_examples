# patterns/sum.py
def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [first, *rest]:
            return first + sum_list(rest)
