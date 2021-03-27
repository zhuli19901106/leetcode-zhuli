# https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# brute force

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        cc = [0 for i in range(n)]
        for i in range(m, n):
            j = i
            while j >= 0 and arr[j] == arr[i]:
                cc[i] += 1
                j -= m
        
        for i in range(m - 1, n):
            cur = cc[i]
            for j in range(m):
                cur = min(cur, cc[i - j])
            if cur >= k:
                return True
        return False
