# hard
# https://leetcode.com/problems/all-oone-data-structure/
# so damn hard
class AllOne:

    def __init__(self):
        self.m1 = {}
        self.m2 = {}
        self.cur_max = -1
        self.cur_min = -1

    def inc(self, key: str) -> None:
        m1 = self.m1
        m2 = self.m2
        cur_max = self.cur_max
        cur_min = self.cur_min

        if not key in m1:
            m1[key] = 0
        m1[key] += 1

        cc = m1[key]
        if cc - 1 in m2 and key in m2[cc - 1]:
            m2[cc - 1].remove(key)
        if cc - 1 in m2 and len(m2[cc - 1]) == 0:
            del m2[cc - 1]

        if not cc in m2:
            m2[cc] = set()
        m2[cc].add(key)

        if cur_max == -1 or cc > cur_max:
            cur_max = cc
        if cur_min == -1 or (not cur_min in m2) or cur_min > cc:
            cur_min = cc
        self.cur_max = cur_max
        self.cur_min = cur_min

    def dec(self, key: str) -> None:
        m1 = self.m1
        m2 = self.m2
        cur_max = self.cur_max
        cur_min = self.cur_min

        cc = m1[key] - 1

        m1[key] -= 1
        if m1[key] == 0:
            del m1[key]

        m2[cc + 1].remove(key)
        if len(m2[cc + 1]) == 0:
            del m2[cc + 1]

        if cc > 0:
            if not cc in m2:
                m2[cc] = set()
            m2[cc].add(key)

        if cur_min - 1 in m2:
            cur_min -= 1
        elif cur_min in m2:
            pass
        elif len(m2) == 0:
            cur_min = -1
        else:
            cur_min += 1
            while not cur_min in m2:
                cur_min += 1

        if len(m2) == 0:
            cur_max = -1
        elif not cur_max in m2:
            cur_max = cc

        self.cur_max = cur_max
        self.cur_min = cur_min

    def getMaxKey(self) -> str:
        if self.cur_max == -1:
            return ''
        return next(iter(self.m2[self.cur_max]))

    def getMinKey(self) -> str:
        if self.cur_min == -1:
            return ''
        return next(iter(self.m2[self.cur_min]))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()