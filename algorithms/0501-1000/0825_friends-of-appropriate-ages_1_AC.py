# medium
# https://leetcode.com/problems/friends-of-appropriate-ages/
# sort and binary search for bounds, corner cases
from bisect import bisect_right

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        a = sorted(ages)
        print(a)
        res = 0
        for x in a:
            low = x / 2 + 7
            high = x
            if low >= high:
                continue
            li = bisect_right(a, low)
            hi = bisect_right(a, high) - 1
            #print(f'low = {low}, high = {high}, li = {li}, hi = {hi}, a[li] = {a[li]}, a[hi] = {a[hi]}')
            # exclude oneself
            res += hi - li
        return res
