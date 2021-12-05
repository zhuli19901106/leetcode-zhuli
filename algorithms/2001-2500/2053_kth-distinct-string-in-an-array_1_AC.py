# https://leetcode.com/problems/kth-distinct-string-in-an-array/
# 1AC
from collections import defaultdict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mm = defaultdict(int)
        for s in arr:
            mm[s] += 1
        idx = 0
        for s in arr:
            if mm[s] != 1:
                continue
            idx += 1
            if idx == k:
                return s
        return ''
