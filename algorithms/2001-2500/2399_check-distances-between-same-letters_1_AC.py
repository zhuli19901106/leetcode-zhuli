# https://leetcode.com/problems/check-distances-between-same-letters/
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        oc = [-1 for i in range(26)]
        for i, c in enumerate(s):
            x = ord(c) - ord('a')
            if oc[x] == -1:
                oc[x] = i
            else:
                oc[x] = abs(i - oc[x]) - 1

        for i in range(26):
            if oc[i] == -1:
                continue
            elif oc[i] != distance[i]:
                return False

        return True
