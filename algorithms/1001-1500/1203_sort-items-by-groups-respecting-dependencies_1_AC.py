# hard
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# do topological sorts on both items and groups
# two graphs
# careful, all groupless items are treated as separate
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        UNUSED_GROUP = -1

        ug = UNUSED_GROUP
        gi = {}
        gg = {}
        for y in range(n):
            if not y in gi:
                gi[y] = set()

            gy = group[y]
            if gy == -1:
                ug -= 1
                gy = ug
            group[y] = gy

            if not gy in gg:
                gg[gy] = set()

            for x in beforeItems[y]:
                if not x in gi:
                    gi[x] = set()
                gx = group[x]
                if gx == -1:
                    ug -= 1
                    gx = ug
                group[x] = gx

                if not gx in gg:
                    gg[gx] = set()

                if gx != gy:
                    gg[gx].add(gy)
                gi[x].add(y)

        ts_gg = self.topological(gg)
        print(f'gg = {gg}')
        print(f'ts_gg = {ts_gg}')
        if len(ts_gg) < len(gg):
            # some groups have cyclic order
            return []
        # record group order
        og = dict([(g, i) for i, g in enumerate(ts_gg)])

        ts_gi = self.topological(gi)
        print(f'gi = {gi}')
        print(f'ts_gi = {ts_gi}')
        if len(ts_gi) < len(gi):
            # some items have cyclic order
            return []
        # record item order
        oi = dict([(x, i) for i, x in enumerate(ts_gi)])

        # sort by (group, item) order
        a = [(og[group[x]], oi[x], x) for x in range(n)]
        a.sort()
        res = [x for _, _, x in a]
        return res

    def topological(self, g):
        ind = {}
        for x in g:
            if not x in ind:
                ind[x] = 0
            for y in g[x]:
                if not y in ind:
                    ind[y] = 0
                ind[y] += 1

        q = deque()
        for x in ind:
            if ind[x] == 0:
                q.appendleft(x)

        res = []
        while len(q) > 0:
            x = q.pop()
            res.append(x)

            if not x in g:
                continue

            for y in g[x]:
                if ind[y] == 0:
                    continue

                ind[y] -= 1
                if ind[y] == 0:
                    q.appendleft(y)

        # return empty if cycle detected
        return res if len(res) == len(ind) else []
