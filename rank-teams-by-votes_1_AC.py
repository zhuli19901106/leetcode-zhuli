# https://leetcode.com/problems/rank-teams-by-votes/
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        nv = len(votes)
        mi = {}
        n = len(votes[0])
        a = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            mi[votes[0][i]] = i

        j0 = ord('A')
        for v in votes:
            for i, c in enumerate(v):
                j = mi[c]
                a[j][i] -= 1

        # alphabetical order
        for i in range(n):
            a[i].append(votes[0][i])

        at = [tuple(x) for x in a]
        at.sort()
        res = []
        for x in at:
            res.append(x[-1])
        return ''.join(res)
