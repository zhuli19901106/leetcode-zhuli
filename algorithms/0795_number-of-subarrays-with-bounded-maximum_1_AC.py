# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# did a bit drawing before getting the idea
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        a = A
        n = len(a)

        def countSmaller(val):
            i = 0
            res = 0
            while i < n:
                if a[i] > val:
                    i += 1
                    continue
                j = i + 1
                while j < n and a[j] <= val:
                    j += 1
                res += (j - i) * (j - i + 1) // 2
                i = j
            return res

        return countSmaller(R) - countSmaller(L - 1)
