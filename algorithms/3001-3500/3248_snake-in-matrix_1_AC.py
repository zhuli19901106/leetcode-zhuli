# easy
# https://leetcode.com/problems/snake-in-matrix/
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        direc = ['UP', 'RIGHT', 'DOWN', 'LEFT']
        mm = dict([(s, i) for i, s in enumerate(direc)])
        offset = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
        
        x, y = 0, 0
        for d in commands:
            i = mm[d]
            x += offset[i][0]
            y += offset[i][1]
        return x * n + y
