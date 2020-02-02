# https://leetcode.com/problems/distance-between-bus-stops/
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            return self.distanceBetweenBusStops(distance, destination, start)
        a = distance
        sa = sum(a)
        s1 = sum(a[start: destination])
        return min(s1, sa - s1)
