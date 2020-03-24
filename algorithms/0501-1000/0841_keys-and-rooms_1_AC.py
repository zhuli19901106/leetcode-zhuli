# https://leetcode.com/problems/keys-and-rooms/
# BFS
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vst = [False for i in range(n)]
        remain = n
        q = deque()

        vst[0] = True
        q.append(0)
        remain -= 1
        while len(q) > 0:
            x = q.popleft()
            for x1 in rooms[x]:
                if vst[x1]:
                    continue
                vst[x1] = True
                remain -= 1
                q.append(x1)
        return remain == 0
