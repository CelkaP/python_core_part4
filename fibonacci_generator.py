import time


def fibonacci_sequence():
    """Function to implement fibonacci sequence generator"""
    f0 = 0
    f1 = 1
    while True:
        yield f0
        tmp = f0
        f0 = f1
        f1 = f1 + tmp
        time.sleep(1)
