# medium
# https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
# 1AC, no surprise
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            if j - i <= 1:
                i = j
                continue
            arr = sorted(cost[i: j])
            res += sum(arr[:-1])
            i = j
        return res
