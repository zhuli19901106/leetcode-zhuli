# https://leetcode.com/problems/counting-words-with-a-given-prefix/
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([w for w in words if w.startswith(pref)])
