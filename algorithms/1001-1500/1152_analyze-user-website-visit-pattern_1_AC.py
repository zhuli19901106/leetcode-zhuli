# https://leetcode.com/problems/analyze-user-website-visit-pattern/
# faithfully implemented
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        stu = set(username)
        a = list(zip(timestamp, username, website))
        a.sort()
        n = len(a)

        mu = {}
        m3 = {}
        for u in stu:
            mu[u] = [tp[2] for i, tp in enumerate(a) if tp[1] == u]
            au = mu[u]
            nu = len(au)
            for i in range(nu):
                for j in range(i + 1, nu):
                    for k in range(j + 1, nu):
                        tp = (au[i], au[j], au[k])
                        if not tp in m3:
                            m3[tp] = set()
                        m3[tp].add(u)
        max_u = max([len(u) for u in m3.values()])
        res = None
        for tp, u in m3.items():
            if len(u) != max_u:
                continue
            if res is None or res > tp:
                res = tp
        return list(res)
