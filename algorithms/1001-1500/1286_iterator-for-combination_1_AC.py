# https://leetcode.com/problems/iterator-for-combination/
# simple idea, ugly implementation, just next permutation, sort of.
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.cl = combinationLength
        self.ac = list(characters)
        self.nc = len(self.ac)
        mc = {}
        for i, c in enumerate(characters):
            mc[c] = i
        self.mc = mc
        self.cc = list(characters[:self.cl])

    def next(self) -> str:
        if self.cc is None:
            return None
        res = ''.join(self.cc)
        if not self.hasNext():
            self.cc = None
        if self.cc is None:
            return res

        i = self.cl - 1
        while i >= 0:
            if self.cc[i] != self.ac[self.nc - self.cl + i]:
                break
            i -= 1
        if i == -1:
            self.cc = None
            return res
        next_i = self.mc[self.cc[i]] + 1
        while i < self.cl:
            self.cc[i] = self.ac[next_i]
            i += 1
            next_i += 1

        return res

    def hasNext(self) -> bool:
        return not self.cc is None

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()