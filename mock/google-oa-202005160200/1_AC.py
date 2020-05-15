class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        i = 0
        na = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if s[i] == 'A':
                na += j - i
            if s[i] == 'L' and j - i > 2:
                return False
            i = j
        return na <= 1
