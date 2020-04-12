# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/514019/Python3-Binary-search-beats-95-time-and-100-memory
# binary search with a forward scan on each iteration, I couldn't have done it better myself
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        mm = {}
        a = nums
        a.sort()
        n = len(a)

        low, high = 0, a[n - 1] - a[0]
        while low < high:
            mid = low + (high - low) // 2
            j = 0
            cc = 0
            for i in range(n):
                while a[i] - a[j] > mid:
                    j += 1
                cc += i - j
            if k > cc:
                low = mid + 1
            else:
                high = mid
        return low
