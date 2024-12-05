# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/
# wrong difficulty
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        mm = {}
        for i in range(min(n, k)):
            if not nums[i] in mm:
                mm[nums[i]] = 1
            else:
                mm[nums[i]] += 1
        res = [self.getXSum(mm, x)]

        for i in range(k, n):
            mm[nums[i - k]] -= 1
            if mm[nums[i - k]] == 0:
                del mm[nums[i - k]]

            if not nums[i] in mm:
                mm[nums[i]] = 1
            else:
                mm[nums[i]] += 1
            res.append(self.getXSum(mm, x))
        return res

    def getXSum(self, mm, x):
        a = []
        for val, cc in mm.items():
            a.append((cc, val))
        a.sort(reverse=True)

        res = 0
        n = len(a)
        for i in range(min(n, x)):
            res += a[i][0] * a[i][1]
        return res
