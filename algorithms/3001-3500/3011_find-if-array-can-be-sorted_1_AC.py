# medium
# https://leetcode.com/problems/find-if-array-can-be-sorted/
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        cb = [self.countBits(x) for x in nums]
        res = []
        n = len(nums)
        i = 0
        while i < n:
            cur = [nums[i]]
            j = i + 1
            while j < n and cb[j] == cb[i]:
                cur.append(nums[j])
                j += 1
            i = j

            cur.sort()
            res += cur

        for i in range(n - 1):
            if res[i] > res[i + 1]:
                return False
        return True

    def countBits(self, x):
        res = 0
        while x != 0:
            x &= x - 1
            res += 1
        return res
