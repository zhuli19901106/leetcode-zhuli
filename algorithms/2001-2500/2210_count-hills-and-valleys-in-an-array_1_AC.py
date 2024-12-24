# easy
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        i, n = 0, len(nums)
        while i < n:
            j = i + 1
            while j < n and nums[i] == nums[j]:
                j += 1
            arr.append(nums[i])
            i = j

        res = 0
        na = len(arr)
        for i in range(1, na - 1):
            # valley
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                res += 1
            # hill
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                res += 1

        return res
