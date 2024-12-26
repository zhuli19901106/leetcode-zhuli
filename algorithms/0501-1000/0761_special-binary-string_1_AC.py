# hard
# https://leetcode.com/problems/special-binary-string/
# like brackets matching
# keep looking for swaps until not found
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        while True:
            s1, found = self.checkSwap(s)
            if not found:
                break
            s = s1
        return s

    def getValidArray(self, s):
        n = len(s)
        valid = [[False for j in range(n)] for i in range(n)]

        for i in range(n - 1):
            if s[i] == '1' and s[i + 1] == '0':
                valid[i][i + 1] = True

        for d in range(4, n + 1, 2):
            for i in range(n - d + 1):
                j = i + d - 1
                if valid[i + 1][j - 1] and (s[i] == '1' and s[j] == '0'):
                    valid[i][j] = True
                    continue

                for k in range(i + 2, j, 2):
                    if valid[i][k - 1] and valid[k][j]:
                        valid[i][j] = True
                        break

        return valid

    def checkSwap(self, s):
        n = len(s)
        valid = self.getValidArray(s)

        for i in range(n):
            for j in range(i + 3, n):
                if not valid[i][j]:
                    continue
                for k in range(i + 2, j):
                    if not (valid[i][k - 1] and valid[k][j]):
                        continue
                    s1, s2 = s[i: k], s[k: j + 1]
                    if s2 + s1 > s1 + s2:
                        s = s[:i] + s2 + s1 + s[j + 1:]
                        return s, True
        return s, False
