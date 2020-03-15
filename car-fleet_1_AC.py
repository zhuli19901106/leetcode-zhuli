# https://leetcode.com/problems/car-fleet/
# https://leetcode.com/problems/car-fleet/discuss/420329/python-concise-solution
# that's smart, I can't figure this out myself
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a = list(zip(map(lambda x: target - x, position), speed))
        a.sort()

        n = len(a)
        min_x, min_s = 0, 1
        res = 0
        for i in range(n):
            x, s = a[i]
            if min_x * s < x * min_s:
                min_x, min_s = x, s
                res += 1
        return res
