# https://leetcode.com/problems/minimum-area-rectangle/
# simple but too slow
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        INT_MAX = 2 ** 31 - 1

        a = sorted([tuple(p) for p in points])
        print(a)
        st = set()
        for p in a:
            st.add((p[0], p[1]))
        n = len(a)
        res = INT_MAX
        for i in range(n):
            for j in range(i + 1, n):
                if a[i][0] >= a[j][0] or a[i][1] >= a[j][1]:
                    continue
                if not (a[i][0], a[j][1]) in st:
                    continue
                if not (a[j][0], a[i][1]) in st:
                    continue
                res = min(res, abs(a[i][0] - a[j][0]) * abs(a[i][1] - a[j][1]))
        return res if res != INT_MAX else 0
