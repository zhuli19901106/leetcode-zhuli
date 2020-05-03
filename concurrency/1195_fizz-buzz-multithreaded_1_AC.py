# https://leetcode.com/problems/fizz-buzz-multithreaded/
# 1AC, barrier, that's a handy one
from threading import Barrier

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.b = Barrier(4)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        n = self.n
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 != 0:
                printFizz()
            self.b.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        n = self.n
        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 == 0:
                printBuzz()
            self.b.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        n = self.n
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                printFizzBuzz()
            self.b.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        n = self.n
        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 != 0:
                printNumber(i)
            self.b.wait()
