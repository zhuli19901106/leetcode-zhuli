# medium
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        a = [capacity[i] - rocks[i] for i in range(n)]
        a.sort()

        res = 0
        cur = additionalRocks
        for x in a:
            if cur < x:
                break
            res += 1
            cur -= x

        return res
