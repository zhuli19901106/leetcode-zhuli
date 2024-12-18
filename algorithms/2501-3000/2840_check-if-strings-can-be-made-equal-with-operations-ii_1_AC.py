# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        tp1 = (''.join(sorted(s1[::2])), ''.join(sorted(s1[1::2])))
        tp2 = (''.join(sorted(s2[::2])), ''.join(sorted(s2[1::2])))
        return tp1 == tp2
