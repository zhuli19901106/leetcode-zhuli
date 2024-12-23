# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/
# should be greedy
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        n = len(word)

        bl = [False for i in range(n)]
        br = [False for i in range(n)]
        for i in range(n - 1):
            bl[i + 1] = self.isAdjacent(word[i + 1], word[i])
            br[i] = self.isAdjacent(word[i], word[i + 1])

        res = 0
        for i in range(1, n - 1):
            if bl[i] and br[i]:
                res += 1
                bl[i] = br[i - 1] = False
                br[i] = bl[i + 1] = False
        for i in range(1, n):
            if bl[i]:
                res += 1
                bl[i] = br[i - 1] = False
        return res

    def isAdjacent(self, c1, c2):
        return abs(ord(c1) - ord(c2)) <= 1
