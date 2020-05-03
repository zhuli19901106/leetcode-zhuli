# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/
# DP solution
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        b2 = 1 << n - 1
        k -= 1
        while b2 > 0:
            i = k // b2
            # invalid count
            if i >= (3 if len(res) == 0 else 2):
                return ''
            k %= b2
            b2 >>= 1

            if len(res) == 0:
                res.append(i)
                continue
            j = 0
            for jj in range(3):
                # skip same char for adjacent position
                if jj == res[-1]:
                    continue
                if j == i:
                    res.append(jj)
                    break
                j += 1
        res = ''.join(map(lambda x: chr(ord('a') + x), res))
        return res
