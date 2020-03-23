# https://leetcode.com/problems/find-anagram-mappings/
# 1AC
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        mb = {}
        for i, v in enumerate(B):
            if not v in mb:
                mb[v] = []
            mb[v].append(i)
        res = []
        for v in A:
            res.append(mb[v].pop())
        return res
