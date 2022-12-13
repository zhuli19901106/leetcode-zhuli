# https://leetcode.com/problems/adding-spaces-to-a-string/
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ns = len(spaces)
        j = 0

        res = []
        for i, c in enumerate(s):
            if j < ns and i == spaces[j]:
                res.append(' ')
                j += 1
            res.append(c)
        res = ''.join(res)

        return res
