from datetime import datetime, timedelta
from functools import lru_cache, wraps
import time

def expiring_lru_cache(seconds, maxsize=128):
    def decorator(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(*args, **kwargs)

        return wrapped
    return decorator

@expiring_lru_cache(4)
def fibonacci(num):
    print(f'  : Miss {num}')
    if num == 0 or num == 1:
        return 1

    return fibonacci(num - 1) + fibonacci(num - 2)

for num, i in enumerate(range(6)):
    print(f"fibonacci({num})")
    result = fibonacci(num)
    print(f"  : result={result}")
    time.sleep(i)
