# easy
# https://leetcode.com/problems/decode-the-message/
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mm = {' ': ' '}
        idx = 0
        for c in key:
            if c in mm or c == ' ':
                continue
            mm[c] = chr(ord('a') + idx)
            idx += 1
        return ''.join([mm[c] for c in message])
