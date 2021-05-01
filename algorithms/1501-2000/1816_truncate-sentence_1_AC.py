# https://leetcode.com/problems/truncate-sentence/
# 1AC
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ws = s.strip().split()
        return ' '.join(ws[: min(k, len(ws))])
