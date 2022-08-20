import sys, time
from functools import lru_cache

# @lru_cache
def fibonacci(num):
    print(f'   -> fibonacci({num})')
    if num == 0 or num == 1:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)


end = 35
# end = int(sys.argv[1])
start = end - 10
print(f'Calculating Fibonacci from {start} to {end}')

for x in range(start, end + 1):
    now = time.perf_counter()
    num = fibonacci(x)
    delta = time.perf_counter() - now
    print(f'{x:3}:{num} ({delta:0.3}s)')
