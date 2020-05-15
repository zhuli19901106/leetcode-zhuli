class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False, i, j
                i += 1
                j -= 1
            return True, -1, -1

        ret, i, j = isPal(s, 0, len(s) - 1)
        if ret:
            return True
        ret, _, _ = isPal(s, i + 1, j)
        if ret:
            return True
        ret, _, _ = isPal(s, i, j - 1)
        if ret:
            return True
        return False
