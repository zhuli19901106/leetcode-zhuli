# medium
# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# 1AC

class SparseVector:
    def __init__(self, nums: List[int]):
        self._vec = {}
        for i, x in enumerate(nums):
            self._vec[i] = x

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if vec is None:
            return 0

        _vec1 = vec._vec
        if len(self._vec) > len(_vec1):
            return vec.dotProduct(self)

        res = 0
        for i, x in self._vec.items():
            if i in _vec1:
                res += x * vec._vec[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)