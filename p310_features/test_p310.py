def sum_list(numbers):
    match numbers:
        case []:
            return 0
        case [int(f) | float(f), int(s) | float(s)]:
            print(f"Here: {f=}, {s=}")
            return f + s
        case [int(f) | float(f), *r]:
            return f + sum_list(r)
        case _:
            raise ValueError("Can only sum lists of numbers")


print(sum_list([]))
print(sum_list([1, 2, 3.432, 99]))
print(sum_list(['a', 'b']))

