# https://leetcode.com/problems/clumsy-factorial/
# a bit clumsy, but OK
# Runtime: 28 ms, faster than 97.56% of Python3 online submissions for Clumsy Factorial.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Clumsy Factorial.
class Solution:
    def clumsy(self, N: int) -> int:
        n = N
        s3 = [0, 1, 2, 0]
        if n < 3:
            return s3[n]

        s1 = 0
        i = n
        while i > 2:
            s1 += i * (i - 1) // (i - 2)
            i -= 4
        s1 = 2 * (n * (n - 1) // (n - 2)) - s1

        t1 = (n - 3) % 4
        t2 = (n - 3)
        nt = (t2 - t1) // 4 + 1
        s2 = (t1 + t2) * nt // 2

        return s1 + s2 - s3[n % 4]
