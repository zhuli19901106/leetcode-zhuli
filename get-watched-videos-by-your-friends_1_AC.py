# https://leetcode.com/problems/get-watched-videos-by-your-friends/
# 1AC, BFS, boring and tiresome
from collections import deque

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        aw = watchedVideos
        af = friends
        n = len(aw)
        mm = {}
        q = deque()
        st = set()

        st.add(id)
        q.append((id, 0))
        while len(q) > 0:
            x, lv = q.popleft()
            if lv == level:
                for vd in aw[x]:
                    if not vd in mm:
                        mm[vd] = [lv, 0]
                    mm[vd][1] += 1

            if lv >= level:
                continue
            for x1 in af[x]:
                if x1 in st:
                    continue
                st.add(x1)
                q.append((x1, lv + 1))

        res = []
        for vd in mm:
            lv, fq = mm[vd]
            if lv == level:
                res.append((fq, vd))
        res.sort()
        res = [x[1] for x in res]
        return res
