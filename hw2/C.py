import functools
import time

def timeout(rps):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **argv):
            t_1 = time.time()
            result = func(*args, **argv)
            t_2 = time.time() - t_1
            if 1/rps - t_2 > 0:
                time.sleep(1/rps - t_2)
            return result
        return wrapper
    return decorator


import time

@timeout(rps=5)
def func():
    pass

if __name__ == "__main__":
    t_start = time.time()
    for i in range(10):
        func()
    t_delta = time.time() - t_start
    print("{:.2f}".format(t_delta))
    print(func.__name__)
