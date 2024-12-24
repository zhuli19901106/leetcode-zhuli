# medium
# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/
# should be "easy"
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        mm = {}
        for i in range(0, n, k):
            s = word[i: i + k]
            if not s in mm:
                mm[s] = 0
            mm[s] += 1
        return n // k - max(mm.values())
