# https://leetcode.com/problems/design-an-ordered-stream/
# 1AC, totally pointless
class OrderedStream:
    def __init__(self, n: int):
        self.mm = {}
        self.idx = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.mm[idKey] = value

        res = []
        if idKey != self.idx:
            return res
        while self.idx in self.mm:
            res.append(self.mm[self.idx])
            self.idx += 1
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)