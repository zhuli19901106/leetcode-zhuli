# medium
# https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/
# tiring
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        a = []
        res = []
        for c in target:
            idx = ord(c) - ord('a')
            a.append('a')
            res.append(''.join(a))

            for j in range(idx):
                a[-1] = chr(ord(a[-1]) + 1)
                res.append(''.join(a))
        return res
