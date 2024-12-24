# easy
# https://leetcode.com/problems/sort-the-people/
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return list(map(lambda x: x[1], sorted(zip(heights, names), reverse=True)))
