# medium
# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
# 1AC, need a bit thinking
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # construct permutation matrix
        ap = [0 for _ in range(n)]
        for i in range(n // 2):
            ap[i] = i * 2
        for i in range(n // 2, n):
            ap[i] = 2 * i - (n - 1)
        
        res = 1
        st = set()
        for i in range(n):
            if i in st:
                continue
            # check for loop length
            j = i
            cnt = 0
            while not j in st:
                st.add(j)
                cnt += 1
                j = ap[j]
            # use LCM to find minimum common loop length
            res = self.lcm(res, cnt)
        return res

    def gcd(self, x, y):
        if x < y:
            return self.gcd(y, x)
        if y == 0:
            return x
        while y > 0:
            x, y = y, x % y
        return x

    def lcm(self, x, y):
        return x * y // self.gcd(x, y)
