# https://leetcode.com/problems/short-encoding-of-words/
# 1AC, suffix matching
# Runtime: 104 ms, faster than 93.33% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Short Encoding of Words.
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ws = sorted([w[::-1] for w in words])
        n = len(ws)
        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and ws[j].startswith(ws[j - 1]):
                j += 1
            res += len(ws[j - 1]) + 1
            i = j
        return res
