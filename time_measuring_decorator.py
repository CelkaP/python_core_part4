import time


def time_measure_decorator(func):
    def wrapper_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken fo function {func}: {(end - start) * 10 ** 3:.03f}ms")

    return wrapper_func


@time_measure_decorator
def generate_using_range():
    """Generate a list using range()"""
    return list(range(100000))


@time_measure_decorator
def generate_using_comprehension():
    """Generate a list using comprehension"""
    return [l for l in range(100000)]


@time_measure_decorator
def generate_using_append():
    """Generate a list using append"""
    my_list = []
    for l in range(100000):
        my_list.append(l)
    return my_list


@time_measure_decorator
def generate_using_concatenation():
    """Generate a list using concatenation"""
    my_list = []
    for l in range(100000):
        my_list = my_list + [l]
    return my_list
