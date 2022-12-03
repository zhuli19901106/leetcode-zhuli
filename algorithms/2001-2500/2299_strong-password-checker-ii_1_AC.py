# https://leetcode.com/problems/strong-password-checker-ii/
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        af = [False, False, False, False, True]
        spec = set(list('!@#$%^&*()-+'))

        for i, c in enumerate(password):
            if c.islower():
                af[0] = True
            if c.isupper():
                af[1] = True
            if c.isdigit():
                af[2] = True
            if c in spec:
                af[3] = True
            if i > 0 and c == password[i - 1]:
                af[4] = False
                break
        for f in af:
            if not f:
                return False
        return True
