# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
# Seriously, I can't think of any but brute-force.
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            bs = bin(i)[2:]
            if S.find(bs) == -1:
                return False
        return True
