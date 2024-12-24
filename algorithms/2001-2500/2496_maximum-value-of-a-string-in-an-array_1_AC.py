# easy
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0
        for s in strs:
            val, is_num = 0, True
            for c in s:
                if c.isdigit():
                    val = val * 10 + ord(c) - ord('0')
                else:
                    is_num = False
                    val = len(s)
                    break
            max_val = max(max_val, val)

        return max_val
