import sys, time
from functools import lru_cache

maxsize = 128
# maxsize = int(sys.argv[1])
depth = 0

@lru_cache(maxsize=maxsize)
def pingala(num):
    global depth
    depth += 1
    print(f'   Miss: {num}, depth={depth}')
    if num <= 7:
        return 1

    return pingala(num - 1) + pingala(num - 2) + pingala(num - 3) \
        + pingala(num - 4) + pingala(num - 5) + pingala(num - 6) \
        + pingala(num - 7)

print(f'Calculating Pingala using a max cache size of {maxsize}')

for x in range(7, 12):
    depth = 0
    now = time.perf_counter()
    num = pingala(x)
    delta = time.perf_counter() - now
    print(f'{x:3}:{num} ({delta:0.3}s)')

print(pingala.cache_info())
