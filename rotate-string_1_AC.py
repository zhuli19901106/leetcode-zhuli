# https://leetcode.com/problems/rotate-string/
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        s = A + A
        return len(A) == len(B) and s.find(B) != -1
