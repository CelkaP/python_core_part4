from fibonacci_iterator import FibonacciIterator
from fibonacci_generator import fibonacci_sequence
from time_measuring_decorator import *


def main():
    fib_iter = FibonacciIterator(max_num=5)

    for num in fib_iter:
        print(num)

    # fib_gen = fibonacci_sequence()

    # for i in fibonacci_sequence():
    #     print(i, end=" ")

    time_measure_decorator(generate_using_range())
    time_measure_decorator(generate_using_comprehension())
    time_measure_decorator(generate_using_append())
    time_measure_decorator(generate_using_append())


if __name__ == "__main__":
    main()
