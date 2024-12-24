# medium
# https://leetcode.com/problems/longest-happy-string/
# tricky, needs a little inspiration
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        res = []
        a = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        a.sort()
        if a[0][0] < 2 * (a[1][0] + a[2][0]) - 2:
            a[0][0] = 2 * (a[1][0] + a[2][0]) - 2
        cc = -a[0][0] - a[1][0] - a[2][0]
        while cc > 0:
            a.sort()
            for i in range(3):
                x, c = a[i]
                if len(res) >= 2 and res[-1] == c and res[-2] == c:
                    continue
                a[i][0] += 1
                res.append(c)
                cc -= 1
                break
        return ''.join(res)
