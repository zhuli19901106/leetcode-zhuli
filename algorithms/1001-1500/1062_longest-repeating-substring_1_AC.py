# medium
# https://leetcode.com/problems/longest-repeating-substring/
# count backward
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        s = S
        n = len(s)
        res = 0
        for i in range(1, n):
            k = n - 1
            j = k - i
            cnt = 0
            while j >= 0:
                if s[j] == s[k]:
                    cnt += 1
                else:
                    cnt = 0
                j -= 1
                k -= 1
                res = max(res, cnt)
        return res
