# easy
# https://leetcode.com/problems/determine-if-two-events-have-conflict/
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])
