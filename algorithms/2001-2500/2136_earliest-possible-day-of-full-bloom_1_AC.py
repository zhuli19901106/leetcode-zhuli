# hard
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        a = list(zip(growTime, plantTime))
        # the key is here
        a.sort(key=lambda x: (-x[0], x[1]))

        n = len(a)
        cur = 0
        fp = [0 for i in range(n)]
        for i in range(n):
            cur += a[i][1]
            fp[i] = cur

        res = 0
        for i in range(n):
            res = max(res, fp[i] + a[i][0])

        return res
