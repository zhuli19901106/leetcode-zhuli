# medium
# https://leetcode.com/problems/find-a-peak-element-ii/
# this is really weird binary search
# after 2h of trying, I give up
# https://algo.monster/liteproblems/1901
# this one is much more intuitive
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        g = mat
        n, m = len(g), len(g[0])

        # so much simpler than my idea
        ll, rr = 0, n - 1
        while ll <= rr:
            mm = ll + (rr - ll >> 1)

            max_val, max_j = g[mm][0], 0
            for j in range(1, m):
                if g[mm][j] > max_val:
                    max_val, max_j = g[mm][j], j
            if mm < n - 1 and g[mm + 1][max_j] > g[mm][max_j]:
                ll = mm + 1
            elif mm > 0 and g[mm - 1][max_j] > g[mm][max_j]:
                rr = mm
            else:
                return [mm, max_j]

        '''
        # bugged and no good
        g = mat
        n, m = len(g), len(g[0])

        # record rows that are already visited
        vst = set()

        r = n // 2
        vst.add(r)
        over = False
        while not over:
            ll, rr = 0, m - 1
            while ll <= rr:
                mm = ll + (rr - ll >> 1)
                cur = g[r][mm]

                bl = (g[r][mm - 1] < cur if mm > 0 else True)
                br = (g[r][mm + 1] < cur if mm < m - 1 else True)
                bt = (g[r - 1][mm] < cur if r > 0 else True)
                bb = (g[r + 1][mm] < cur if r < n - 1 else True)

                print(f'r = {r} ll = {ll} rr = {rr} mm = {mm} vst = {vst}')
                print(f'bl = {bl} br = {br} bt = {bt} bb = {bb}\n')

                # peak of this row
                if bl and br:
                    if bt and bb:
                        # found the 2D peak
                        return [r, mm]
                    elif not bt and not r - 1 in vst:
                        r -= 1
                        vst.add(r)
                        break
                    elif not bb and not r + 1 in vst:
                        r += 1
                        vst.add(r)
                        break
                    else:
                        over = True
                        break
                elif not bl and not br:
                    ll += 1
                elif not bl:
                    rr = mm
                else:
                    ll = mm + 1

        return [-1, -1]
        '''
