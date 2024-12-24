# medium
# https://leetcode.com/problems/path-sum-iv/
# 1AC, what's the point?
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        nodes = {}
        leaves = set()
        for x in nums:
            depth = x // 100 % 10 - 1
            row_id = x // 10 % 10 - 1
            val = x % 10
            node_id = (1 << depth) + row_id
            nodes[node_id] = val
            leaves.add(node_id)
            if (node_id >> 1) in nodes:
                nodes[node_id] += nodes[node_id >> 1]
            if (node_id >> 1) in leaves:
                leaves.remove(node_id >> 1)
        res = 0
        for x in leaves:
            res += nodes[x]
        return res
