# medium
# https://leetcode.com/problems/the-kth-factor-of-n/
# 1AC, easy?
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        af = []
        i = 1
        while i <= n // i:
            if n % i != 0:
                i += 1
                continue
            af.append(i)
            if i != n // i:
                af.append(n // i)
            i += 1
        af.sort()
        return af[k - 1] if k <= len(af) else -1
