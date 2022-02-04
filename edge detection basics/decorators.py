import time

def time_it(func):
    def time_func(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - start
        print(f"time to execute the '{func.__name__}' function: {total_time}s")
        return result
    return time_func