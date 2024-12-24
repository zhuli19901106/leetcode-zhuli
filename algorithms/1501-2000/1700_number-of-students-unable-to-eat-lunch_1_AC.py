# easy
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# 1AC, simulation
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque()
        cs = [0, 0]
        for x in students:
            q.append(x)
            cs[x] += 1
        for x in sandwiches:
            if cs[x] == 0:
                break
            while True:
                y = q.popleft()
                if y == x:
                    cs[x] -= 1
                    break
                else:
                    q.append(y)
        return len(q)
