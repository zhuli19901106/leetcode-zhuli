# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mw = {}
        ml = {}
        for x, y in matches:
            if x in mw:
                mw[x] += 1
            else:
                mw[x] = 1
            if y in ml:
                ml[y] += 1
            else:
                ml[y] = 1

        aw = []
        for x in mw:
            if not x in ml:
                aw.append(x)
        aw.sort()

        al = []
        for y in ml:
            if ml[y] == 1:
                al.append(y)
        al.sort()

        return [aw, al]
