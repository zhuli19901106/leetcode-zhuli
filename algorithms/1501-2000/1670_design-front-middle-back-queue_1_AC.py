# https://leetcode.com/problems/design-front-middle-back-queue/
# laborious
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.n = 0

    def pushFront(self, val: int) -> None:
        self.q1.appendleft(val)

        if len(self.q1) > len(self.q2):
            x = self.q1.pop()
            self.q2.appendleft(x)

        self.n += 1

    def pushMiddle(self, val: int) -> None:
        self.q1.append(val)

        if len(self.q1) > len(self.q2):
            x = self.q1.pop()
            self.q2.appendleft(x)

        self.n += 1

    def pushBack(self, val: int) -> None:
        self.q2.append(val)

        if len(self.q1) + 1 < len(self.q2):
            x = self.q2.popleft()
            self.q1.append(x)

        self.n += 1

    def popFront(self) -> int:
        if self.n == 0:
            return -1
        if self.n == 1:
            self.n -= 1
            return self.q2.pop()

        val = self.q1.popleft()

        if len(self.q1) + 1 < len(self.q2):
            x = self.q2.popleft()
            self.q1.append(x)

        self.n -= 1

        return val

    def popMiddle(self) -> int:
        if self.n == 0:
            return -1
        if self.n == 1:
            self.n -= 1
            return self.q2.pop()

        if len(self.q1) < len(self.q2):
            val = self.q2.popleft()
        else:
            val = self.q1.pop()

        self.n -= 1

        return val

    def popBack(self) -> int:
        if self.n == 0:
            return -1
        if self.n == 1:
            self.n -= 1
            return self.q2.pop()

        val = self.q2.pop()

        if len(self.q1) > len(self.q2):
            x = self.q1.pop()
            self.q2.appendleft(x)

        self.n -= 1

        return val

    def _print(self):
        print(f'n={self.n}, q1={self.q1}, q2={self.q2}')

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()