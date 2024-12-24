# medium
# https://leetcode.com/problems/k-th-symbol-in-grammar/
# 1AC
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        a = []
        K -= 1
        while N > 1:
            a.append(K)
            K >>= 1
            N -= 1
        n = len(a)
        f = 0
        for i in range(n - 1, -1, -1):
            if a[i] & 1:
                f = 1 - f
        return f
