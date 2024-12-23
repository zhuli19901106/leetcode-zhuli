# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            return -self.maxPermutation(-num)
        else:
            return self.minPermutation(num)

    def maxPermutation(self, x):
        return int(''.join(sorted(str(x), reverse=True)))

    def minPermutation(self, x):
        if x == 0:
            return x

        s = []
        c0 = 0
        for c in str(x):
            if c == '0':
                c0 += 1
            else:
                s.append(c)
        s.sort()
        s = ''.join(s)
        s = s[0] + ('0' * c0) + s[1:]

        return int(s)
