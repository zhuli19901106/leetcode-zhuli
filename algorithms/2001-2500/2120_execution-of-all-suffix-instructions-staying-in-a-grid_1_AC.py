# https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/
# 1AC, the O(m) solution is too brainy, I give up

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dir = {'L': (0, -1), 'R': (0, +1), 'U': (-1, 0), 'D': (+1, 0)}

        # pure simulation
        res = []
        m = len(s)
        for i in range(m):
            x, y = startPos
            cc = 0
            for j in range(i, m):
                x, y = x + dir[s[j]][0], y + dir[s[j]][1]
                if not (x >= 0 and x <= n - 1 and y >= 0 and y <= n - 1):
                    break
                cc += 1
            res.append(cc)
        return res
