# medium
# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/
# a variant of anagram
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        if n % k != 0:
            return False

        m = n // k
        sa = [s[i * m: (i + 1) * m] for i in range(k)]
        ta = [t[i * m: (i + 1) * m] for i in range(k)]
        sa.sort()
        ta.sort()

        return sa == ta
