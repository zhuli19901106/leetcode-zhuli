# medium
# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
# 1AC, BFS
from collections import defaultdict, deque

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mm = defaultdict(lambda: set())
        for x, y in adjacentPairs:
            mm[x].add(y)
            mm[y].add(x)
        n = len(adjacentPairs) + 1

        st = set()
        q = deque()
        for x in mm:
            if len(mm[x]) != 1:
                continue
            st.add(x)
            q.append(x)
            break

        res = []
        while len(q) > 0:
            x = q.popleft()
            res.append(x)
            for x1 in mm[x]:
                if x1 in st:
                    continue
                st.add(x1)
                q.append(x1)
        return res
