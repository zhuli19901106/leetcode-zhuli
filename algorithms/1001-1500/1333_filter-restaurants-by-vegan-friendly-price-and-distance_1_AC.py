# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
# what's this? a sql test?
# I'm sure you'll see a whole bunch of one-liner here
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]],\
        veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        a1 = [(x[0], x[1]) for x in restaurants if\
            ((veganFriendly == 1 and x[2] == 1) or (veganFriendly == 0)) and\
            (x[3] <= maxPrice and x[4] <= maxDistance)]
        a2 = sorted(a1, key=lambda x: (-x[1], -x[0]))
        return list(map(lambda x: x[0], a2))
