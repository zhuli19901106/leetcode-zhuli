# https://leetcode.com/problems/destroying-asteroids/
# isn't this that ad game "hero war"?
# should be easy
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for ast in asteroids:
            if mass >= ast:
                mass += ast
            else:
                return False
        return True
