# https://leetcode.com/explore/interview/card/apple/351/design/3138/
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.mst = []

    def push(self, x: int) -> None:
        self.st.append(x)
        if len(self.mst) == 0 or x <= self.mst[-1]:
            self.mst.append(x)

    def pop(self) -> None:
        x = self.st.pop()
        if x == self.mst[-1]:
            self.mst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mst[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
