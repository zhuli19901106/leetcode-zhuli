# https://leetcode.com/problems/grumpy-bookstore-owner/
# range sum, fixed window size
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        c = customers
        n = len(c)
        c1 = [c[i] if grumpy[i] == 1 else 0 for i in range(n)]
        c2 = [c[i] if grumpy[i] == 0 else 0 for i in range(n)]

        res = sum(c2)
        ps_c1 = [0 for i in range(n + 1)]
        for i in range(n):
            ps_c1[i + 1] = ps_c1[i] + c1[i]
        extra = 0
        for i in range(X, n + 1):
            extra = max(extra, ps_c1[i] - ps_c1[i - X])
        res += extra
        return res
