# medium
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
# 1AC, prefix and postfix

from collections import defaultdict

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        lt = len(target)
        mpre = defaultdict(int)
        mpost = defaultdict(int)
        half = 0
        for i, s in enumerate(nums):
            ls = len(s)
            bpre, bpost = False, False

            if target.startswith(s):
                mpre[ls] += 1
                bpre = True
            if target.endswith(s):
                mpost[ls] += 1
                bpost = True
            if bpre and bpost and 2 * ls == lt:
                half += 1

        res = 0
        for i in range(1, lt):
            if i in mpre and lt - i in mpost:
                res += mpre[i] * mpost[lt - i]
        res -= half

        return res
