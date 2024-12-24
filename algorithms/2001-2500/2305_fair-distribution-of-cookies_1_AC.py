# medium
# https://leetcode.com/problems/fair-distribution-of-cookies/
# nasty code, sorry

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort()
        nc = len(cookies)
        vst = [False for i in range(nc)]

        def dfs(idx, cc, ki, ak):
            if idx == nc:
                if ki < k - 1:
                    if len(ak) >= 2 and ak[-1] < ak[-2]:
                        return -1

                    ak.append(0)
                    ret = dfs(0, cc, ki + 1, ak)
                    ak.pop()
                    return ret
                else:
                    if cc < nc:
                        return -1
                    return max(ak)

            res = -1

            ret = dfs(idx + 1, cc, ki, ak)
            if ret != -1 and (res == -1 or res > ret):
                res = ret

            if not vst[idx]:
                vst[idx] = True
                ak[-1] += cookies[idx]
                ret = dfs(idx + 1, cc + 1, ki, ak)
                ak[-1] -= cookies[idx]
                vst[idx] = False
                if ret != -1 and (res == -1 or res > ret):
                    res = ret

            return res

        return dfs(0, 0, 0, [0])
