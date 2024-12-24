# easy
# https://leetcode.com/problems/slowest-key/
# the duration shouldn't be summed up
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        last = 0
        mm = {}
        for i, c in enumerate(keysPressed):
            dur = releaseTimes[i] - last
            last = releaseTimes[i]
            if not c in mm:
                mm[c] = dur
            else:
                mm[c] = max(mm[c], dur)
        max_dur = 0
        for k, v in mm.items():
            max_dur = max(max_dur, v)
        res = ''
        for k, v in mm.items():
            if v == max_dur and k >= res:
                res = k
        return res
