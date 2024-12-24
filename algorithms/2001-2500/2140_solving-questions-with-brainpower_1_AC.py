# medium
# https://leetcode.com/problems/solving-questions-with-brainpower/
# the local + global DP problem
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        qs = questions
        n = len(qs)

        loc = [0 for i in range(n)]
        gl = [0 for i in range(n)]

        loc[n - 1] = qs[n - 1][0]
        gl[n - 1] = loc[n - 1]

        for i in range(n - 2, -1, -1):
            j = i + qs[i][1] + 1

            loc[i] = qs[i][0]
            if j <= n - 1:
                loc[i] += gl[j]
            gl[i] = max(gl[i + 1], loc[i])

        return gl[0]
