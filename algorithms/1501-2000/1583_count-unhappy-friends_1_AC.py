# https://leetcode.com/problems/count-unhappy-friends/
# by voting this is a totally BS problem, thus let's slip by at minimal cost
# 217 ups and 706 downs, now that's a view
# not demanding and really confusing

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        res = set()
        mp = {}
        for x, y in pairs:
            mp[x] = y
            mp[y] = x
        mh = []
        for i in range(n):
            mh.append({})
            for j, x in enumerate(preferences[i]):
                mh[i][x] = j

        def checkHappyPairing(x):
            y = mp[x]
            for y1 in preferences[x]:
                if y1 == y:
                    break
                x1 = mp[y1]
                if not (x1 in mh[y1] and x in mh[y1]):
                    continue
                ix = mh[y1][x]
                ix1 = mh[y1][x1]
                if ix < ix1:
                    return False
            return True

        for x, y in pairs:
            if not checkHappyPairing(x):
                res.add(x)
            if not checkHappyPairing(y):
                res.add(y)

        return len(res)
