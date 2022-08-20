import sys

def fibonacci(num):
    if num == 0 or num == 1:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)


end = int(sys.argv[1])
start = end - 10
print(f'Calculating Fibonacci from {start} to {end}')

for x in range(start, end + 1):
    num = fibonacci(x)
    print(num)
