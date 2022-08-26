def fizzbuzz_if(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzbuzz'
    elif n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'buzz'
    else:
        return n


def fizzbuzz_case(n):
    mod_3 = n % 3
    mod_5 = n % 5

    match (mod_3, mod_5):
        case (0, 0):
            return 'fizzbuzz'
        case (_, 0):
            return 'buzz'
        case (0, _):
            return 'fizz'
        case (_, _):
            return n


for f in (fizzbuzz_if, fizzbuzz_case):
    assert f(3) == 'fizz', f(3)
    assert f(5) == 'buzz', f(5)
    assert f(15) == 'fizzbuzz', f(15)
    assert f(14) == 14, f(14)
