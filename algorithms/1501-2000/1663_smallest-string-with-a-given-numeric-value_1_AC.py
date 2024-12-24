# medium
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
# just be greedy
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = [1 for _ in range(n)]
        k -= n
        i = n - 1
        while k > 0:
            if k >= 25:
                res[i] += 25
                k -= 25
            else:
                res[i] += k
                k = 0
            i -= 1
        res = ''.join([chr(ord('a') + x - 1) for x in res])
        return res
