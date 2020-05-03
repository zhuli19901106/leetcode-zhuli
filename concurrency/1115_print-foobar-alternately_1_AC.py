# https://leetcode.com/problems/print-foobar-alternately/
# 1AC, barrier and lock
from threading import Barrier, Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.b = Barrier(2)
        self.lk = Lock()
        self.lk.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            # ensure order within each round
            self.lk.release()
            # ensure order between rounds
            self.b.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lk.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.b.wait()
