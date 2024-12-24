# easy
# https://leetcode.com/problems/shuffle-string/
# 1AC
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        mm = dict(zip(indices, list(range(n))))
        rev_indices = [mm[i] for i in range(n)]
        return ''.join([s[rev_indices[i]] for i in range(n)])
