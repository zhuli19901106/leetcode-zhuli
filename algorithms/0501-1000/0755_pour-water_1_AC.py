# medium
# https://leetcode.com/problems/pour-water/
# 1AC, fill one by one, rather clumsy
class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        h = heights
        n = len(h)
        for _ in range(V):
            i = K
            while i > 0 and h[i - 1] <= h[i]:
                i -= 1
            j = i
            while j < K and h[j + 1] == h[j]:
                j += 1
            if j < K:
                h[j] += 1
                continue

            i = K
            while i < n - 1 and h[i + 1] <= h[i]:
                i += 1
            j = i
            while j > K and h[j - 1] == h[j]:
                j -= 1
            if j > K:
                h[j] += 1
                continue

            h[K] += 1
        return h
