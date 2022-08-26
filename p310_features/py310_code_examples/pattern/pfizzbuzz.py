# pattern/pfizzbuzz.py
def fizzbuzz(number):
    mod_3 = number % 3
    mod_5 = number % 5

    match (mod_3, mod_5):
        case (0, 0):
            return "fizzbuzz"
        case (_, 0):
            return "buzz"
        case (0, _):
            return "fizz"
        case _:
            return str(number)
