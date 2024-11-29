# https://leetcode.com/problems/number-of-senior-citizens/
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([x for x in [int(s[11: 13]) for s in details] if x > 60])
