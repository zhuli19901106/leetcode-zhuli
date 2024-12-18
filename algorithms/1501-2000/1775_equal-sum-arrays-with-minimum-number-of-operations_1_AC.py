# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
# don't make things more complicated than they have to be
# it's greedy
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        a1, sm1 = self.countDice(nums1)
        a2, sm2 = self.countDice(nums2)

        res = 0

        if sm1 > sm2:
            a1, a2 = a2, a1
            sm1, sm2 = sm2, sm1
        elif sm1 == sm2:
            return res

        gap = sm2 - sm1
        # alternatively
        for i in range(5):
            d = 5 - i

            # i + 1 to 6 for a1
            if d * a1[i] < gap:
                res += a1[i]
                gap -= d * a1[i]
            else:
                res += (gap + d - 1) // d
                gap = 0
            if gap == 0:
                return res

            # 6 - i to 1 for a2
            if d * a2[5 - i] < gap:
                res += a2[5 - i]
                gap -= d * a2[5 - i]
            else:
                res += (gap + d - 1) // d
                gap = 0
            if gap == 0:
                return res
        return -1

    def countDice(self, nums):
        sm = 0
        a = [0 for i in range(6)]
        for x in nums:
            a[x - 1] += 1
            sm += x
        return a, sm
