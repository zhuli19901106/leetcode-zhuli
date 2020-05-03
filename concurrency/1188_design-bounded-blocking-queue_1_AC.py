# https://leetcode.com/problems/design-bounded-blocking-queue/
# 1AC, gradually getting the hang of it
from collections import deque
from threading import Semaphore

class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.q = deque()
        self.cap = capacity
        self.sem_empty = Semaphore(0)
        self.sem_full = Semaphore(self.cap)

    def enqueue(self, element: int) -> None:
        self.sem_full.acquire()
        self.q.append(element)
        self.sem_empty.release()

    def dequeue(self) -> int:
        self.sem_empty.acquire()
        res = self.q.popleft()
        self.sem_full.release()
        return res

    def size(self) -> int:
        return len(self.q)
