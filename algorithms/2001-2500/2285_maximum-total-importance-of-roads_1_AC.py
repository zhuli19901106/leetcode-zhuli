# medium
# https://leetcode.com/problems/maximum-total-importance-of-roads/
# greedy

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0 for i in range(n)]
        for x, y in roads:
            deg[x] += 1
            deg[y] += 1
        a = list(zip(deg, range(n)))
        a.sort(key=lambda x: -x[0])

        aw = [0 for i in range(n)]
        j = n
        for d, i in a:
            aw[i] = j
            j -= 1

        res = 0
        for x, y in roads:
            res += aw[x] + aw[y]

        return res
