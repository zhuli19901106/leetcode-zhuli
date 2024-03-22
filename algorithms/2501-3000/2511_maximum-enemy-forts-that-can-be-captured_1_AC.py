# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        res = 0

        n = len(forts)
        i = 0
        pos = [i for i, x in enumerate(forts) if x == 1 or x == -1]

        for i in range(len(pos) - 1):
            if forts[pos[i]] * forts[pos[i +1]] < 0:
                res = max(res, pos[i + 1] - pos[i] - 1)

        return res
