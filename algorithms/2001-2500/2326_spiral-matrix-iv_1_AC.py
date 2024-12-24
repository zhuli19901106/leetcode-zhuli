# medium
# https://leetcode.com/problems/spiral-matrix-iv/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        offs = [(0, +1), (+1, 0), (0, -1), (-1, 0)]
        next_dir = [1, 2, 3, 0]

        cur_dir = 0
        x, y = 0, 0
        p = head
        res = [[0 for j in range(n)] for i in range(m)]
        vst = [[False for j in range(n)] for i in range(m)]
        for _ in range(n * m):
            if p:
                val = p.val
                p = p.next
            else:
                val = -1
            res[x][y] = val
            vst[x][y] = True
            for di in range(4):
                x1, y1 = x + offs[cur_dir][0], y + offs[cur_dir][1]
                if x1 < 0 or x1 > m - 1 or y1 < 0 or y1 > n - 1 or vst[x1][y1]:
                    cur_dir = next_dir[cur_dir]
                    continue
                break
            x, y = x1, y1

        return res
