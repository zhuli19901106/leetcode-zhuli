# medium
# https://leetcode.com/problems/can-make-palindrome-from-substring/
# 1AC, long story, at least I made it.
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def countOne(x):
            res = 0
            while x != 0:
                x = (x & x - 1)
                res += 1
            return res

        res = []
        # bit mask for 26 chars
        bm = [0]
        for c in s:
            idx = ord(c) - ord('a')
            bm.append(bm[-1] ^ (1 << idx))
        for x, y, k in queries:
            # count how many chars appear odd number of times
            cur_bm = bm[y + 1] ^ bm[x]
            cnt = countOne(cur_bm)

            res.append(k >= cnt // 2)
        return res
