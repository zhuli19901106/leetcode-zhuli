# medium
# https://leetcode.com/problems/find-missing-observations/
# no trick
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # sum of n dices
        m = len(rolls)
        sm = (n + m) * mean - sum(rolls)
        if sm < n or sm > 6 * n:
            return []

        q, r = sm // n, sm % n
        return [q + 1 for i in range(r)] + [q for i in range(n - r)]
