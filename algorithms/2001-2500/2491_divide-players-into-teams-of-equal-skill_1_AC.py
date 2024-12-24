# medium
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        a = sorted(skill)
        n = len(a) // 2
        sm = 0
        for x in a:
            sm += x
        if sm % n != 0:
            return -1
        target = sm // n

        res = 0
        i = 0
        j = 2 * n - 1
        while i < j:
            if a[i] + a[j] != target:
                return -1
            res += a[i] * a[j]
            i += 1
            j -= 1

        return res
