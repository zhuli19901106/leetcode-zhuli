# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len([x for x in nums if x % 3 != 0])
