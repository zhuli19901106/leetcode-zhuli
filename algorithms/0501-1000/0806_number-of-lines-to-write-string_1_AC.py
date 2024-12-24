# easy
# https://leetcode.com/problems/number-of-lines-to-write-string/
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        MAX_LEN = 100
        cur_len = 0
        nl = 1
        for c in S:
            w = widths[ord(c) - ord('a')]
            if cur_len + w > MAX_LEN:
                nl += 1
                cur_len = w
            else:
                cur_len += w
        return [nl, cur_len]
