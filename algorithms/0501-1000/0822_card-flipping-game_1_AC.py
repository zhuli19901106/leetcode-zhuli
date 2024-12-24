# medium
# https://leetcode.com/problems/card-flipping-game/
# 1AC, mind twister
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        af = fronts
        ab = backs
        st = set()
        n = len(af)
        for i in range(n):
            if af[i] == ab[i]:
                st.add(af[i])
        for i in range(n):
            if ab[i] in st and not af[i] in st:
                af[i], ab[i] = ab[i], af[i]
        for i in range(n):
            if af[i] < ab[i] and not af[i] in st:
                af[i], ab[i] = ab[i], af[i]
        st = set(af)

        INT_MAX = 2 ** 31 - 1
        res = INT_MAX
        for x in ab:
            if not x in st:
                res = min(res, x)
        res = 0 if res == INT_MAX else res
        return res
