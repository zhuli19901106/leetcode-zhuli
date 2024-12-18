# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/
class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)

        a = []
        i = 0
        while i < n:
            while i < n and s[i] != '1':
                i += 1

            if i == n:
                break

            j = i + 1
            while j < n and s[j] == '1':
                j += 1
            a.append(j - i)

            i = j

        res = 0
        sm = 0
        for x in a:
            sm += x
            res += sm

        # if there's no 0 at the end of string, no need for the last shift
        if s[n - 1] == '1':
            res -= sm

        return res
