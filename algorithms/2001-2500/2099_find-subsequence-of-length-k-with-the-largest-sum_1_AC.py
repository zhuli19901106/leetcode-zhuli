# easy
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# 1AC

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ai = [(x, i) for i, x in enumerate(nums)]
        ai.sort()
        ai_topk = ai[-k:]
        ai_topk.sort(key=lambda tp: tp[1])

        return [tp[0] for tp in ai_topk]
