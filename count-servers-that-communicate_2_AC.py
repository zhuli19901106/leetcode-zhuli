# https://leetcode.com/problems/count-servers-that-communicate/
# reverse thinking
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        a = grid
        n = len(a)
        m = len(a[0])
        ar = [0 for i in range(n)]
        ac = [0 for j in range(m)]
        res = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    ar[i] += 1
                    ac[j] += 1
                    res += 1
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1 and ar[i] == 1 and ac[j] == 1:
                    res -= 1
        return res
