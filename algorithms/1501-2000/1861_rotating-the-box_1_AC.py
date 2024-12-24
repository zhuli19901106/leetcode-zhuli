# medium
# https://leetcode.com/problems/rotating-the-box/
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        b = box
        m, n = len(b), len(b[0])

        for i in range(m):
            j = n - 1
            while j >= 0:
                if b[i][j] != '#':
                    j -= 1
                    continue

                j1 = j - 1
                while j1 >=0 and b[i][j1] == '#':
                    j1 -= 1

                off = 0
                while j + off + 1 <= n - 1 and b[i][j + off + 1] == '.':
                    off += 1

                if off == 0:
                    j = j1
                    continue
                while j > j1:
                    b[i][j + off] = b[i][j]
                    j -= 1
                for k in range(j1 + 1, j1 + off + 1):
                    b[i][k] = '.'

        res = [[b[m - 1 - i][j] for i in range(m)] for j in range(n)]

        return res

    def print(self, box):
        for r in box:
            print(''.join(r))
        print('')
