# https://leetcode.com/problems/previous-permutation-with-one-swap/
# too sloppy, not cool
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        a = A[:]
        n = len(a)
        i = n - 2
        while i >= 0 and a[i] <= a[i + 1]:
            i -= 1
        if i < 0:
            return a

        j = i + 1
        while j < n:
            k = j + 1
            while k < n and a[k] == a[j]:
                k += 1
            if k < n and a[k] < a[i]:
                j = k
            else:
                break

        a[i], a[j] = a[j], a[i]
        return a
