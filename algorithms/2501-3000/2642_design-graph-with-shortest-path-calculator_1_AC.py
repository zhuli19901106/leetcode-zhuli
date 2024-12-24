# hard
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
# why are there so many graph questions?
# no repeated edges
from heapq import heappush, heappop

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = {}

        g = self.g
        for x in range(n):
            g[x] = {}
        for x, y, w in edges:
            g[x][y] = w

    def addEdge(self, edge: List[int]) -> None:
        x, y, w = edge
        self.g[x][y] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        # just do a Dijkstra if the cost is acceptable
        g = self.g

        dist = {}
        pq = []
        vst = set()

        dist[node1] = 0
        heappush(pq, (0, node1))
        while len(pq) > 0:
            d, x = heappop(pq)
            if x in vst:
                continue
            vst.add(x)

            for y, w in g[x].items():
                if y in vst:
                    continue
                if (not y in dist) or dist[x] + w < dist[y]:
                    dist[y] = dist[x] + w
                    heappush(pq, (dist[y], y))

            if node2 in vst:
                break

        return dist[node2] if node2 in dist else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)