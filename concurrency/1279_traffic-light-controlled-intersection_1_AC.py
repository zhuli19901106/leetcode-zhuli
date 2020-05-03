# https://leetcode.com/problems/traffic-light-controlled-intersection/
# 1AC, well, it's a bit confusing when you leave out the time series logic
from threading import BoundedSemaphore

class TrafficLight:
    def __init__(self):
        self.sem = BoundedSemaphore(1)
        # same with road ID
        self.state = 1

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        with self.sem:
            if self.state != roadId:
                self.state = roadId
                turnGreen()
            crossCar()
