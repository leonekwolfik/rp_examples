from functools import wraps
import time

def how_long(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = time.perf_counter()
        result = func(*args, **kwargs)
        delta = time.perf_counter() - now
        print(f"@how_long({func.__name__}) -> {delta:0.3}s")
        return result

    return wrapper

@how_long
def pingala(num):
    if num <= 7:
        return 1

    return pingala(num - 1) + pingala(num - 2) + pingala(num - 3) \
        + pingala(num - 4) + pingala(num - 5) + pingala(num - 6) \
        + pingala(num - 7)


num = pingala(8)
print(num)
