# https://leetcode.com/problems/richest-customer-wealth/
# 1AC
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sm = -1
        for a in accounts:
            max_sm = max(max_sm, sum(a))
        return max_sm
