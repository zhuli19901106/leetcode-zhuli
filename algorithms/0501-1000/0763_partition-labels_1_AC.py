# https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        m1 = {}
        m2 = {}
        for i, c in enumerate(S):
            if not c in m1:
                m1[c] = i
            m2[c] = i
        res = []
        n = len(S)
        last_i = i = j = 0
        while i < n:
            j = max(j, m2[S[i]])
            if i == j:
                res.append(j - last_i + 1)
                last_i = i + 1
            i += 1
        return res
