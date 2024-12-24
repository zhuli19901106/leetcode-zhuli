# medium
# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        mc = {}
        idx = 0
        for fc in favoriteCompanies:
            for c in fc:
                if not c in mc:
                    mc[c] = idx
                    idx += 1

        a = [set([mc[c] for c in fc]) for fc in favoriteCompanies]

        res = []
        n = len(a)
        for i in range(n):
            sub = False
            for j in range(n):
                if j == i:
                    continue

                if len(a[i]) > len(a[j]):
                    continue

                if len(a[i] & a[j]) == len(a[i]):
                    # a[i] is a subset of a[j]
                    # NOTE: subset, not proper subset
                    sub = True
                    break
            if not sub:
                res.append(i)

        return res
