# medium
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
# medium?
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]
        n = len(pref)
        for i in range(1, n):
            res.append(pref[i - 1] ^ pref[i])

        return res
