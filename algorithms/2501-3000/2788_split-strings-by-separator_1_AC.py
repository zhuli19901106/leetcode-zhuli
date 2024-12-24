# easy
# https://leetcode.com/problems/split-strings-by-separator/
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for w in words:
            res += [s for s in w.split(separator) if len(s) > 0]
        return res
