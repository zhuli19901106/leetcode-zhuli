# https://leetcode.com/problems/hand-of-straights/
# devil's in the detail, what's the hurry :(
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        a = hand
        n = len(a)
        st = sorted(set(a))
        m = dict(zip(st, [0 for i in range(len(st))]))
        for x in a:
            m[x] += 1
        for x in st:
            while m[x] > 0:
                i = 0
                while i < W:
                    if x + i in m and m[x + i] > 0:
                        m[x + i] -= 1
                    else:
                        break
                    i += 1
                if i < W:
                    return False
        return True
