# easy
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        cur = groups[0]
        n = len(words)
        for i in range(1, n):
            if groups[i] == cur:
                continue
            res.append(words[i])
            cur = 1 - cur
        return res
