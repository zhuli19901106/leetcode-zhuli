# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
class Solution:
    def checkString(self, s: str) -> bool:
        last_a, first_b = -1, -1
        for i, c in enumerate(s):
            if c == 'a':
                last_a = i
                continue
            if c == 'b' and first_b == -1:
                first_b = i
                continue

        return last_a == -1 or first_b == -1 or last_a < first_b
