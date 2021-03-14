# https://leetcode.com/problems/build-an-array-with-stack-operations/
# 1AC, pointless
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        j = 0
        res = []
        for i in range(1, n + 1):
            if i == target[j]:
                res.append('Push')
                j += 1
            else:
                res.append('Push')
                res.append('Pop')
            if j == len(target):
                break
        return res
