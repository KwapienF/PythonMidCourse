import time
import functools

def wrapper1(a_func):
    def func_with_wrapper(*args, **kwargs):
        start = time.time()
        result = a_func(*args, **kwargs)
        stop = time.time()
        time1 = stop - start
        print(f'Function {a_func.__name__} took {time1} to be done')
        return result
    return func_with_wrapper


@wrapper1
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v

print(get_sequence(10))

