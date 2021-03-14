# https://leetcode.com/problems/design-parking-system/
# 1AC
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.arr_cnt = [0 for _ in range(3)]
        self.arr_cap = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        carType -= 1
        if self.arr_cnt[carType] >= self.arr_cap[carType]:
            return False
        self.arr_cnt[carType] += 1
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)