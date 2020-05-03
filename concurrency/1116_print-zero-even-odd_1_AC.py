# https://leetcode.com/problems/print-zero-even-odd/
# 1AC, barrier and lock
from threading import Barrier, Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.b = Barrier(3)
        self.lk = Lock()
        self.lk.acquire()

	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            printNumber(0)
            self.lk.release()
            self.b.wait()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.lk.acquire()
                printNumber(i)
            self.b.wait()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 != 0:
                self.lk.acquire()
                printNumber(i)
            self.b.wait()
