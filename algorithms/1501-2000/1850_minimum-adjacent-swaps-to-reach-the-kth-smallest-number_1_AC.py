# medium
# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
# 1AC, I can only do it with bruteforce for now
# I'd say it's rather tiring and sloppy to do the whole simulation
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        a1 = list(num)
        a2 = a1[:]
        for i in range(k):
            self.nextPermutation(a2)
        return self.countSwap(a1, a2)

    def nextPermutation(self, a):
        n = len(a)
        i = n - 2
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1
        if i < 0:
            return
        j = i + 1
        while j + 1 < n and a[i] < a[j + 1]:
            j += 1
        a[i], a[j] = a[j], a[i]
        a[i + 1:] = a[i + 1:][::-1]

    def countSwap(self, a1, a2):
        n = len(a1)
        res = 0
        i = 0
        while i < n:
            if a2[i] == a1[i]:
                i += 1
                continue
            j = i + 1
            while a2[j] != a1[i]:
                j += 1
            while j > i:
                a2[j], a2[j - 1] = a2[j - 1], a2[j]
                j -= 1
                res += 1
            i += 1
        return res
