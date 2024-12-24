# medium
# https://leetcode.com/problems/construct-string-with-repeat-limit/
# be greedy, be careful
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        MAXC = 26
        sa = ''.join([chr(ord('a') + i) for i in range(MAXC - 1, -1, -1)])

        mm = {}
        for c in s:
            if not c in mm:
                mm[c] = 0
            mm[c] += 1

        res = []
        n = len(s)
        last = ''
        while n > 0:
            found = False
            for c in sa:
                # must pick a different available char
                if c in mm and c != last:
                    found = True
                    break
            if not found:
                break

            if last in mm and last > c:
                k = 1
            else:
                k = min(mm[c], repeatLimit)
            n -= k

            if mm[c] <= k:
                del mm[c]
            else:
                mm[c] -= k
            res.append(c * k)

            last = c

        res = ''.join(res)
        return res
