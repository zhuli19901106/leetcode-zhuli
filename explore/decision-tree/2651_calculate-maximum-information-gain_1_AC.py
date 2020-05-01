# https://leetcode.com/explore/learn/card/decision-tree/285/implementation/2651/
from collections import defaultdict
from math import log2

class Solution:
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        def entropy(a):
            if len(a) == 0:
                return 0.0

            mm = defaultdict(lambda: 0)
            for x in a:
                mm[x] += 1
            vs = list(mm.values())
            sm = sum(vs)
            ps = [x / sm for x in vs]
            return sum([-p * log2(p) for p in ps])
        
        sp = sorted(set(petal_length))
        h0 = entropy(species)
        n = len(species)
        max_g = 0
        for x in sp:
            s1, s2 = [], []
            for i in range(n):
                if petal_length[i] <= x:
                    s1.append(species[i])
                else:
                    s2.append(species[i])
            h1 = entropy(s1) * len(s1) / n
            h2 = entropy(s2) * len(s2) / n
            max_g = max(max_g, h0 - h1 - h2)
        return max_g
