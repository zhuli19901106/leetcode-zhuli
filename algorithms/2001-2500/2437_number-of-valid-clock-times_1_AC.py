# https://leetcode.com/problems/number-of-valid-clock-times/
class Solution:
    def countTime(self, time: str) -> int:
        hh = time[:2]
        mm = time[3:5]

        nh = 1
        if hh[0] == '?':
            nh = 24 if hh[1] == '?' else 3 if (hh[1] >= '0' and hh[1] <= '3') else 2
        else:
            nh = (4 if hh[1] == '?' else 1) if hh[0] == '2' else (10 if hh[1] == '?' else 1)

        nm = 1
        if mm[0] == '?':
            nm = 60 if mm[1] == '?' else 6
        else:
            nm = 10 if mm[1] == '?' else 1

        return nh * nm
