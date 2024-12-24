# hard
# https://leetcode.com/problems/maximum-frequency-stack/
# https://leetcode.com/problems/maximum-frequency-stack/discuss/597386/Python-O(1)-with-clear-variable-names
# couldn't make of why my solution was slow and tricky, but this one is really clever
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.mi = defaultdict(list)
        self.mc = defaultdict(lambda: 0)
        self.mxc = 0

    def push(self, x: int) -> None:
        mi = self.mi
        mc = self.mc

        mc[x] += 1
        mi[mc[x]].append(x)
        self.mxc = max(self.mxc, mc[x])

    def pop(self) -> int:
        mi = self.mi
        mc = self.mc

        x = mi[self.mxc].pop()
        if len(mi[self.mxc]) == 0:
            self.mxc -= 1
        mc[x] -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
