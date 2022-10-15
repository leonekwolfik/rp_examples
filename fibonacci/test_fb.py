def fibonacci_of(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci_of(n - 1) + fibonacci_of(n - 2)


for i in range(15):
    print(fibonacci_of(i))
