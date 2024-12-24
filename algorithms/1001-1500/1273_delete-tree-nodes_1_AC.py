# medium
# https://leetcode.com/problems/delete-tree-nodes/
# 1AC, simple and intuitive
class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        n = nodes
        tr = [[] for i in range(n)]
        for i, x in enumerate(parent):
            if x == -1:
                continue
            tr[x].append(i)
        ts = value[:]
        nc = [1 for i in range(n)]

        def traverse(i):
            nonlocal ts, nc

            for j in tr[i]:
                traverse(j)
                if ts[j] == 0:
                    nc[j] = 0
                ts[i] += ts[j]
                nc[i] += nc[j]
            if ts[i] == 0:
                nc[i] = 0

        traverse(0)
        return nc[0]
