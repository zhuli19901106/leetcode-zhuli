# medium
# https://leetcode.com/problems/max-consecutive-ones-iii/
# sliding window
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        a = A
        n = len(a)
        k = K
        i = j = 0
        res = 0
        cnt = 0
        for i in range(n):
            if a[i] == 0:
                cnt += 1
            while cnt > k:
                if a[j] == 0:
                    cnt -= 1
                j += 1
            res = max(res, i - j + 1)
        return res
