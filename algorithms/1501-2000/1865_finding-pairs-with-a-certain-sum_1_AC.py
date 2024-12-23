# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
# with nums1 small and nums2 large, it's obvious
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.mm2 = {}
        self.nums1 = nums1[:]
        self.nums2 = nums2[:]

        mm2 = self.mm2
        for x in nums2:
            if not x in mm2:
                mm2[x] = 0
            mm2[x] += 1

    def add(self, index: int, val: int) -> None:
        nums2 = self.nums2
        x = nums2[index]
        nums2[index] += val

        mm2 = self.mm2
        if not x + val in mm2:
            mm2[x + val] = 0
        mm2[x + val] += 1

        mm2[x] -= 1
        if mm2[x] == 0:
            del mm2[x]

    def count(self, tot: int) -> int:
        nums1 = self.nums1
        mm2 = self.mm2

        res = 0
        for x in nums1:
            if tot - x in mm2:
                res += mm2[tot - x]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)