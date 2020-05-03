# https://leetcode.com/problems/print-in-order/
# 1AC, that's mind-boggling
from threading import Lock

class Foo:
    def __init__(self):
        self.locks = [Lock() for i in range(2)]
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.locks[0].acquire()
        printSecond()
        self.locks[0].release()
        self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.locks[1].acquire()
        printThird()
        self.locks[1].release()
