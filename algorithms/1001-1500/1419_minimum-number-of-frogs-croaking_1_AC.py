# https://leetcode.com/problems/minimum-number-of-frogs-croaking/
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # prepare 4 queues for c r o a k, not 5
        mm = dict([(c, i) for i, c in enumerate('croak')])
        a = [0 for i in range(4)]

        res = 0
        for c in croakOfFrogs:
            if not c in mm:
                return -1
            i = mm[c]

            if i == 0:
                a[i] += 1
            elif i == 4:
                if a[3] == 0:
                    return -1
                else:
                    a[3] -= 1
            else:
                if a[i - 1] == 0:
                    return -1
                else:
                    a[i - 1] -= 1
                    a[i] += 1

            res = max(res, sum(a))

        for i in range(4):
            if a[i] != 0:
                return -1
        return res
