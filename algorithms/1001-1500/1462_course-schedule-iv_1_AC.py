# medium
# https://leetcode.com/problems/course-schedule-iv/
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = {}
        for x, y in prerequisites:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)

        succ = {}
        for x in g:
            if x in succ:
                continue
            self.traverse(x, g, succ)

        res = [(x in succ and y in succ[x]) for x, y in queries]
        return res

    def traverse(self, x, g, succ):
        xs = set()

        for y in g.get(x, set()):
            xs.add(y)
            if not y in succ:
                ys = self.traverse(y, g, succ)
            else:
                ys = succ[y]
            xs |= ys
        succ[x] = xs
        return succ[x]
