# https://leetcode.com/problems/hash-divided-string/
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        res = []
        for i in range(0, n, k):
            res.append(self.hashStr(s[i:i + k]))
        res = ''.join(res)
        return res

    def hashStr(self, s):
        sm = 0
        for c in s:
            sm += ord(c) - ord('a')
        sm %= 26
        return chr(ord('a') + sm)
