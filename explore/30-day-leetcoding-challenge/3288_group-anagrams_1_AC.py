# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
# 1AC
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mm = defaultdict(list)
        for s in strs:
            mm[''.join(sorted(s))].append(s)
        return list(mm.values())
