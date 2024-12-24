# easy
# https://leetcode.com/problems/sort-even-and-odd-indices-independently/
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a1, a2 = nums[0::2], nums[1::2]
        a1.sort()
        a2.sort(reverse=True)

        res = []
        n = len(nums)
        for i in range(n):
            if i % 2 == 0:
                res.append(a1[i // 2])
            else:
                res.append(a2[(i - 1) // 2])

        return res
