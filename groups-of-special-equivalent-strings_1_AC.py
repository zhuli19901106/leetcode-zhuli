# https://leetcode.com/problems/groups-of-special-equivalent-strings/
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def getEquivalent(s):
            return ''.join(sorted(s[0::2]) + sorted(s[1::2]))

        a = [getEquivalent(s) for s in A]
        eg = set()
        for s in a:
            eg.add(s)
        return len(eg)
