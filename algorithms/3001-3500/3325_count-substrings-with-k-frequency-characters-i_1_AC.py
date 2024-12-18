# https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/
# sliding window
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        mm = {}
        n = len(s)

        res = 0
        j = 0
        for i in range(n):
            c = s[i]
            if not c in mm:
                mm[c] = 0
            mm[c] += 1

            while j <= i and max(mm.values()) >= k:
                mm[s[j]] -= 1
                if mm[s[j]] == 0:
                    del mm[s[j]]
                j += 1
            res += i - j + 1
        res = n * (n + 1) // 2 - res

        return res
