# https://leetcode.com/problems/koko-eating-bananas/
# binary search
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def eatAll(a, k):
            res = 0
            for x in a:
                res += (x + k - 1) // k
            return res

        if H >= sum(piles):
            return 1
        low = 1
        high = max(piles)
        while low + 1 < high:
            mid = low + (high - low) // 2
            h = eatAll(piles, mid)
            if h > H:
                low = mid
            else:
                high = mid
        return high
