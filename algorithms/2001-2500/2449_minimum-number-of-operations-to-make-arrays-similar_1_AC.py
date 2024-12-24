# hard
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/
# mind twister

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        arr_ne = [x for x in nums if x % 2 == 0]
        arr_no = [x for x in nums if x % 2 == 1]
        arr_te = [x for x in target if x % 2 == 0]
        arr_to = [x for x in target if x % 2 == 1]
        arr_ne.sort()
        arr_no.sort()
        arr_te.sort()
        arr_to.sort()

        ne = len(arr_ne)
        no = len(arr_no)
        ce = sum([(arr_ne[i] - arr_te[i]) // 2 for i in range(ne) if arr_ne[i] > arr_te[i]])
        co = sum([(arr_no[i] - arr_to[i]) // 2 for i in range(no) if arr_no[i] > arr_to[i]])

        return ce + co
