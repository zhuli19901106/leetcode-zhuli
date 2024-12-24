# medium
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mm = {}
        for x in arr:
            if x in mm:
                mm[x] += 1
            else:
                mm[x] = 1

        ac = sorted(mm.items(), key=lambda x: x[1])

        res = len(ac)
        cur = k
        for x, cc in ac:
            if cur >= cc:
                cur -= cc
                res -= 1
            else:
                break

        return res
