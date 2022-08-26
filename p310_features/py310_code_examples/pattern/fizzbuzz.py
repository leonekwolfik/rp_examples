# pattern/fizzbuzz.py
def fizzbuzz(number):
    mod_3 = number % 3
    mod_5 = number % 5

    if mod_3 ==0 and mod_5 == 0:
        return "fizzbuzz"
    elif mod_5 == 0:
        return "buzz"
    elif mod_3 == 0:
        return "fizz"
    else:
        return str(number)
