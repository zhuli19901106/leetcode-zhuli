# https://leetcode.com/problems/watering-plants/
# 1AC, pure simulation

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        if plants is None or len(plants) == 0:
            return 0
        if capacity < max(plants):
            return -1

        pos, vol = -1, capacity
        res = 0
        for i, x in enumerate(plants):
            if vol >= x:
                res += abs(i - pos)
                vol -= x
            else:
                res += abs(pos + 1) + abs(i + 1)
                vol = capacity - x
            pos = i

        return res
