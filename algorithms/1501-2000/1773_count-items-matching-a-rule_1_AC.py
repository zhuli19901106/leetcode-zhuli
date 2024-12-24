# easy
# https://leetcode.com/problems/count-items-matching-a-rule/
# 1AC
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mp = {'type': 0, 'color': 1, 'name': 2}
        ri = mp[ruleKey]
        res = 0
        for x in items:
            if x[ri] == ruleValue:
                res += 1
        return res
