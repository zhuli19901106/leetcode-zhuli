# easy
# https://leetcode.com/problems/minimize-string-length/description/
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
