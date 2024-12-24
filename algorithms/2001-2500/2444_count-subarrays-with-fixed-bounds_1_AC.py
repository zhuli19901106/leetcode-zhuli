# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# it must be sliding window, so it is
# quite the trouble
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        if minK == maxK:
            return self.countSubarraysOne(nums, minK)

        n = len(nums)
        res = 0
        i = 0
        while i < n:
            if nums[i] < minK or nums[i] > maxK:
                i += 1
                continue

            seg = []
            j = i
            while j < n and nums[j] >= minK and nums[j] <= maxK:
                seg.append(nums[j])
                j += 1
            res += self.countSubarraysTwo(seg, minK, maxK)
            i = j

        return res

    def countSubarraysOne(self, nums, x):
        n = len(nums)
        res = 0
        i = 0
        while i < n:
            if nums[i] != x:
                i += 1
                continue

            j = i
            while j < n and nums[j] == x:
                j += 1
            k = j - i
            res += k * (k + 1) // 2
            i = j

        return res

    def countSubarraysTwo(self, nums, x, y):
        n = len(nums)

        res = 0
        cx, cy = 0, 0
        j = 0
        for i in range(n):
            if nums[i] == x:
                cx += 1
            elif nums[i] == y:
                cy += 1

            while j < i and cx > 0 and cy > 0:
                if nums[j] == x:
                    cx -= 1
                elif nums[j] == y:
                    cy -= 1
                j += 1
            res += j

        return res
