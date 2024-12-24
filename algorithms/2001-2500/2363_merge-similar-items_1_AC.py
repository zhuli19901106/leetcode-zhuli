# easy
# https://leetcode.com/problems/merge-similar-items/
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        def collect(mm, items):
            for v, w in items:
                if v in mm:
                    mm[v] += w
                else:
                    mm[v] = w

        mm = {}
        collect(mm, items1)
        collect(mm, items2)
        ret = sorted(mm.items())

        return ret
