# medium
# https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mm = {}
        for i, c in enumerate(S):
            mm[c] = i
        res = []
        n = len(S)
        last_i = i = j = 0
        while i < n:
            j = max(j, mm[S[i]])
            if i == j:
                res.append(j - last_i + 1)
                last_i = i + 1
            i += 1
        return res
