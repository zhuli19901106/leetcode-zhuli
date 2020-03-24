# https://leetcode.com/problems/buddy-strings/
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        n = len(A)
        if A == B:
            return len(set(A)) < n
        diff = [ord(A[i]) - ord(B[i]) for i in range(n) if A[i] != B[i]]
        return len(diff) == 2 and sum(diff) == 0
