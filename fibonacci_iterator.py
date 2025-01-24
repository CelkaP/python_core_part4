class FibonacciIterator:
    """
    Class to implement fibonacci iterator
    """

    def __init__(self, max_num=0):
        self.max = max_num
        self.n = 0
        self.f0 = 0
        self.f1 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        tmp = self.f0
        self.f0 = self.f1
        self.f1 = self.f1 + tmp
        self.n += 1
        return tmp
