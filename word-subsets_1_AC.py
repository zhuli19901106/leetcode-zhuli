# https://leetcode.com/problems/word-subsets/
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(s):
            m = {}
            for c in s:
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
            return m

        mb = {}
        for b in B:
            mbb = count(b)
            for c in mbb:
                if c in mb:
                    mb[c] = max(mb[c], mbb[c])
                else:
                    mb[c] = mbb[c]

        res = []
        for a in A:
            ma = count(a)
            i = 0
            for c in mb:
                if c in ma and ma[c] >= mb[c]:
                    i += 1
                else:
                    break
            if i == len(mb):
                res.append(a)
        return res
