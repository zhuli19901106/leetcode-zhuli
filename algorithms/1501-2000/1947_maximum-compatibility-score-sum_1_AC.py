# https://leetcode.com/problems/maximum-compatibility-score-sum/
# simple idea, though

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])
        mask = (1 << n) - 1

        def calcScore(x, y):
            val = (~(x ^ y)) & mask
            res = 0
            while val != 0:
                val &= val - 1
                res += 1
            return res

        ast = []
        for a in students:
            val = 0
            for x in a:
                val = (val << 1) + x
            ast.append(val)

        ame = []
        for a in mentors:
            val = 0
            for x in a:
                val = (val << 1) + x
            ame.append(val)

        def dfs(idx, score, vst):
            if idx == m:
                return score

            res = -1
            for i in range(m):
                if i in vst:
                    continue
                vst.add(i)
                cur_res = dfs(idx + 1, score + calcScore(ast[idx], ame[i]), vst)
                res = max(res, cur_res)
                vst.remove(i)

            return res

        res = dfs(0, 0, set())

        return res
