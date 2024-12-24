# medium
# https://leetcode.com/problems/search-suggestions-system/
from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        a = sorted(products)
        na = len(a)
        res = []
        n = len(searchWord)
        for i in range(n):
            sw = searchWord[: i + 1]
            idx = bisect_left(a, sw)
            single_res = []
            for i in range(3):
                if idx + i < na and a[idx + i].startswith(sw):
                    single_res.append(a[idx + i])
            if len(single_res) == 0:
                break
            else:
                res.append(single_res)
        while len(res) < n:
            res.append([])
        return res
