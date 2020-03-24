# https://leetcode.com/problems/find-the-town-judge/
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ind = [0 for i in range(N)]
        outd = [0 for i in range(N)]
        for x, y in trust:
            outd[x - 1] += 1
            ind[y - 1] += 1
        for i in range(N):
            if ind[i] == N - 1 and outd[i] == 0:
                return i + 1
        return -1
