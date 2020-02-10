# https://leetcode.com/problems/add-to-array-form-of-integer/
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        a = A[::-1]
        k = list(str(K))[::-1]
        for i in range(len(a), max(len(a), len(k)) + 1):
            a.append(0)
        for i in range(len(k)):
            a[i] += ord(k[i]) - ord('0')
        for i in range(len(a) - 1):
            a[i + 1] += a[i] // 10
            a[i] %= 10
        while len(a) > 1 and a[-1] == 0:
            a.pop()
        return a[::-1]
