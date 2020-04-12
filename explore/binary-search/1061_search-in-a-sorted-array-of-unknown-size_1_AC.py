# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
# 1AC, binary search
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    INT_MAX = 2147483647

    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        low = 0
        high = 2 ** 31 - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            val = reader.get(mid)
            if val == Solution.INT_MAX:
                high = mid
            else:
                low = mid
        n = high

        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            val = reader.get(mid)
            if target < val:
                high = mid - 1
            elif target > val:
                low = mid + 1
            else:
                return mid
        return -1
