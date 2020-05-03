# https://leetcode.com/problems/building-h2o/
# man, that's puzzling
from threading import Semaphore

class H2O:
    def __init__(self):
        self.hsem = Semaphore(0)
        self.osem = Semaphore(0)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.osem.release()
        self.hsem.acquire()
        releaseHydrogen()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.osem.acquire()
        self.osem.acquire()
        releaseOxygen()
        self.hsem.release()
        self.hsem.release()
