# https://leetcode.com/problems/validate-binary-tree-nodes/
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indeg = [0 for i in range(n)]
        outdeg = [0 for i in range(n)]
        for arr in leftChild, rightChild:
            for i, x in enumerate(arr):
                if x == -1:
                    continue
                outdeg[i] += 1
                indeg[x] += 1
        root_num = 0
        for x in indeg:
            if x == 0:
                root_num += 1
            if x > 1:
                return False
        if root_num != 1:
            return False
        for x in outdeg:
            if x > 2:
                return False
        return True
