# https://leetcode.com/problems/ambiguous-coordinates/
# just do the searching
# Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Ambiguous Coordinates.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Ambiguous Coordinates.
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def possibleNum(s):
            n = len(s)
            if s[-1] == '0':
                if s[0] == '0':
                    return ['0'] if n == 1 else []
                return [s]
            if s[0] == '0':
                return [s[:1] + '.' + s[1:]]
            res = [s]
            for i in range(1, n):
                res.append(s[:i] + '.' + s[i:])
            return res

        s = S[1:-1]
        n = len(s)
        res = []
        for i in range(1, n):
            s1 = s[:i]
            r1 = possibleNum(s1)
            if len(r1) == 0:
                continue
            s2 = s[i:]
            r2 = possibleNum(s2)
            if len(r2) == 0:
                continue
            for ss1 in r1:
                for ss2 in r2:
                    res.append(f'({ss1}, {ss2})')
        return res
