# https://leetcode.com/problems/describe-the-painting/
# if the max value isn't too large, it's acceptable
# a simple suffix sum with sets will MLE
# use dict and set to make it sparse
from sortedcontainers import SortedDict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # must be sorted to accumulate sums
        a = SortedDict()

        for x, y, c in segments:
            if not x in a:
                a[x] = 0
            if not y in a:
                a[y] = 0
            a[x] += c
            a[y] -= c

        res = []
        last_x = 0
        sm = 0
        for x, cc in a.items():
            if sm > 0:
                # the points inbetween are irrelevant
                res.append([last_x, x, sm])
            sm += cc
            last_x = x
        return res
'''
from sortedcontainers import SortedDict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # max_val = max([y for x, y, _c in segments])
        # a = [set() for i in range(max_val + 1)]
        a = SortedDict()

        for x, y, c in segments:
            if not x in a:
                a[x] = set()
            if not y in a:
                a[y] = set()
            a[y].add(c)
            a[x].add(-c)

        na = len(a)
        for i in range(na - 2, -1, -1):
            # suffix sum
            st, st1 = a[a.iloc[i]], a[a.iloc[i + 1]]
            for x1 in st1:
                if not -x1 in st:
                    st.add(x1)
                else:
                    st.remove(-x1)

        res = []
        for i in range(na - 1):
            x, x1 = a.iloc[i], a.iloc[i + 1]
            st, st1 = a[a.iloc[i]], a[a.iloc[i + 1]]
            if sum(st1) == 0:
                # skip empty intervals
                continue

            res.append([x, x1, sum(st1)])

        return res
'''
