# https://leetcode.com/problems/count-prefixes-of-a-given-string/
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return len([w for w in words if s.startswith(w)])
