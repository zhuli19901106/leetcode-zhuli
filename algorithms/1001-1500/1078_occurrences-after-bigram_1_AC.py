# easy
# https://leetcode.com/problems/occurrences-after-bigram/
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr = text.strip().split(' ')
        n = len(arr)
        res = []
        for i in range(n - 2):
            if arr[i] == first and arr[i + 1] == second:
                res.append(arr[i + 2])
        return res
