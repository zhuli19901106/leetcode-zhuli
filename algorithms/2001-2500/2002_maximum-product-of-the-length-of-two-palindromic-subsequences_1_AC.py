# medium
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
# bruteforce search, slow but acceptable
# can be a bit faster using bit ops
class Solution:
    def maxProduct(self, s: str) -> int:
        res = [0]
        self.dfs(s, 0, '', '', res)
        return res[0]

    def dfs(self, s, i, s1, s2, res):
        if len(s1) > 0 and len(s2) > 0 \
            and self.isPalidrome(s1) and self.isPalidrome(s2):
            res[0] = max(res[0], len(s1) * len(s2))

        if i == len(s):
            return
        self.dfs(s, i + 1, s1, s2, res)
        self.dfs(s, i + 1, s1 + s[i], s2, res)
        self.dfs(s, i + 1, s1, s2 + s[i], res)

    def isPalidrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
