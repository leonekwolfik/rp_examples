from functools import wraps
import time

def how_longer(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.perf_counter()
            result = func(*args, **kwargs)
            delta = time.perf_counter() - now
            print(f"@how_longer({func.__name__})")
            print(f"   : {message}")
            print(f"   : {delta:0.3}s")
            return result

        return wrapper
    return decorator

@how_longer("Fibonacci, who?")
def pingala(num):
    if num <= 7:
        return 1

    return pingala(num - 1) + pingala(num - 2) + pingala(num - 3) \
        + pingala(num - 4) + pingala(num - 5) + pingala(num - 6) \
        + pingala(num - 7)


num = pingala(8)
print(num)
