# https://leetcode.com/problems/max-stack/
# 1AC, given the usual max stack, I can't come up with an all-O(1) solution, even in an ammortized manner.
# might as well keep it simple and make do
# popMax is an O(n) operation
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.max_st = []

    def push(self, x: int) -> None:
        st = self.st
        max_st = self.max_st
        st.append(x)
        if len(max_st) == 0 or max_st[-1] <= x:
            max_st.append(x)

    def pop(self) -> int:
        st = self.st
        max_st = self.max_st
        res = st.pop()
        if max_st[-1] == res:
            max_st.pop()
        return res

    def top(self) -> int:
        st = self.st
        return st[-1]

    def peekMax(self) -> int:
        max_st = self.max_st
        return max_st[-1]

    def popMax(self) -> int:
        st = self.st
        max_st = self.max_st
        res = self.peekMax()
        tmp = []
        while st[-1] != res:
            tmp.append(st.pop())

        st.pop()
        max_st.pop()
        while len(tmp) > 0:
            self.push(tmp.pop())
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()