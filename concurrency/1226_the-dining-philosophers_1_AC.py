# https://leetcode.com/problems/the-dining-philosophers/
# 1AC, one of the most classic in the history of parellel computing
from threading import Semaphore, Lock

class DiningPhilosophers:
    def __init__(self, n=5):
        self.n = n
        # deadlock prevention
        self.ne = Semaphore(n - 1)
        # chopsticks on a round table
        self.lk = [Lock() for i in range(n)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        self.ne.acquire()
        i = philosopher

        self.lk[i].acquire()
        self.lk[(i + 1) % self.n].acquire()
        pickLeftFork()
        pickRightFork()

        eat()

        putLeftFork()
        putRightFork()
        self.lk[i].release()
        self.lk[(i + 1) % self.n].release()

        self.ne.release()
