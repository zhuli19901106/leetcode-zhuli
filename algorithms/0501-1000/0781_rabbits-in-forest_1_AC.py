# medium
# https://leetcode.com/problems/rabbits-in-forest/
# Runtime: 36 ms, faster than 91.46% of Python3 online submissions for Rabbits in Forest.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Rabbits in Forest.
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        m = {}
        for x in answers:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        res = 0
        for k, v in m.items():
            k += 1
            res += (v + k - 1) // k * k
        return res
