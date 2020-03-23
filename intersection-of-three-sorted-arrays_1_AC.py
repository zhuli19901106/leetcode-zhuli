# https://leetcode.com/problems/intersection-of-three-sorted-arrays/
# 1AC
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        a = Solution.intersect(arr1, arr2)
        a = Solution.intersect(a, arr3)
        return a

    @staticmethod
    def intersect(a1, a2):
        n1 = len(a1)
        n2 = len(a2)
        res = []
        i = j = 0
        while i < n1 and j < n2:
            if a1[i] < a2[j]:
                i += 1
            elif a1[i] > a2[j]:
                j += 1
            else:
                res.append(a1[i])
                i += 1
                j += 1
        return res
