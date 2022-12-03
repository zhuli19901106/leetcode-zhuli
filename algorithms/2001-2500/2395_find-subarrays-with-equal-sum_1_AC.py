# https://leetcode.com/problems/find-subarrays-with-equal-sum/
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        st = set()
        for i in range(len(nums) - 1):
            val = nums[i] + nums[i + 1]
            if val in st:
                return True
            st.add(val)
        return False
