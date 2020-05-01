# https://leetcode.com/explore/learn/card/decision-tree/285/implementation/2650/
class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        a = input
        if len(a) == 0:
            return 0.0

        mm = defaultdict(lambda: 0)
        for x in a:
            mm[x] += 1
        vs = list(mm.values())
        sm = sum(vs)
        ps = [x / sm for x in vs]
        return sum([-p * log2(p) for p in ps])
