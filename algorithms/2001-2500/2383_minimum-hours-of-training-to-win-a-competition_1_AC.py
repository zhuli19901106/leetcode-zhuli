# easy
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        cur_ng, cur_xp = initialEnergy, initialExperience
        res = 0

        n = len(energy)
        for i in range(n):
            ng, xp = energy[i], experience[i]

            if cur_ng <= ng:
                res += ng + 1 - cur_ng
                cur_ng = ng + 1
            cur_ng -= ng

            if cur_xp <= xp:
                res += xp + 1 - cur_xp
                cur_xp = xp + 1
            cur_xp += xp

        return res
