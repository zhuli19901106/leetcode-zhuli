# https://leetcode.com/problems/partition-array-according-to-given-pivot/
# naive approach
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        t1, t2 = [], []
        cc = 0
        for x in nums:
            if x < pivot:
                t1.append(x)
            elif x > pivot:
                t2.append(x)
            else:
                cc += 1
        j = 0
        for x in t1:
            nums[j] = x
            j += 1
        for i in range(cc):
            nums[j] = pivot
            j += 1
        for x in t2:
            nums[j] = x
            j += 1

        return nums
