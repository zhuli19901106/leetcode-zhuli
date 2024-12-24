# easy
# https://leetcode.com/problems/longest-nice-substring/
# 1AC, can't think of any efficient solution except brute force
# simulation with bit manipulation
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res = ''
        f = True
        for i in range(n):
            arr = [0 for i in range(26)]
            cc = 0
            for j in range(i, n):
                if s[j].islower():
                    k = ord(s[j]) - ord('a')
                    b = 1
                else:
                    k = ord(s[j]) - ord('A')
                    b = 2

                if arr[k] & b == 0:
                    if arr[k] | b == 3:
                        cc -= 1
                    else:
                        cc += 1
                    arr[k] |= b

                if cc == 0 and j - i + 1 > len(res):
                    res = s[i: j + 1]
        return res
