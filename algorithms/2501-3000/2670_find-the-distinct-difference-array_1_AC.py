# easy
# https://leetcode.com/problems/find-the-distinct-difference-array/
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pref = set()
        suf = {}
        for x in nums:
            if not x in suf:
                suf[x] = 1
            else:
                suf[x] += 1

        res = []
        for x in nums:
            pref.add(x)
            suf[x] -= 1
            if suf[x] == 0:
                del suf[x]
            res.append(len(pref) - len(suf))
        return res
