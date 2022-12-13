# https://leetcode.com/problems/reachable-nodes-with-restrictions/
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def traverse(g, x, nodes_res, nodes_vst):
            nodes_vst.add(x)
            if not x in g:
                return
            for y in g[x]:
                if y in nodes_res or y in nodes_vst:
                    continue
                traverse(g, y, nodes_res, nodes_vst)

        g = {}
        for x, y in edges:
            if not x in g:
                g[x] = set()
            if not y in g:
                g[y] = set()
            g[x].add(y)
            g[y].add(x)
        nodes_res = set(restricted)
        nodes_vst = set()
        traverse(g, 0, nodes_res, nodes_vst)

        return len(nodes_vst)
