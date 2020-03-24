# https://leetcode.com/problems/index-pairs-of-a-string/
# 1AC, just brute-force
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        st = set(words)
        n = len(text)
        for i in range(n):
            for j in range(i + 1, n + 1):
                tt = text[i: j]
                if not tt in st:
                    continue
                res.append([i, j - 1])
        return res
