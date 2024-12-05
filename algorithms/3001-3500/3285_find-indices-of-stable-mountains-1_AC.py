# https://leetcode.com/problems/find-indices-of-stable-mountains/
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        n = len(height)
        return [i for i in range(1, n) if height[i - 1] > threshold]
