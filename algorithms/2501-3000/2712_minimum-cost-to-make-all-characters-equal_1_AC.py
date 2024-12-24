# medium
# https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/
# it's a deque, both ends
# always choose the smaller end
class Solution:
    def minimumCost(self, s: str) -> int:
        a = []
        n = len(s)
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
            a.append(j - i)
            i = j

        res = 0
        i = 0
        j = len(a) - 1
        while i < j:
            if a[i] < a[j]:
                res += a[i]
                a[i + 1] += a[i]
                i += 1
            else:
                res += a[j]
                a[j - 1] += a[j]
                j -= 1
        return res
