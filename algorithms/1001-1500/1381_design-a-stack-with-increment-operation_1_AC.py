# medium
# https://leetcode.com/problems/design-a-stack-with-increment-operation/
# Runtime: 76 ms, faster than 99.53% of Python3 online submissions for Design a Stack With Increment Operation.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Design a Stack With Increment Operation.
class CustomStack:
    def __init__(self, maxSize: int):
        self.cap = maxSize
        self.arr = []

    def push(self, x: int) -> None:
        arr = self.arr
        n = len(arr)
        if n >= self.cap:
            return
        if n > 0:
            arr[-1] -= x
        arr.append(x)

    def pop(self) -> int:
        arr = self.arr
        n = len(arr)
        if n == 0:
            return -1
        x = arr.pop()
        if n > 1:
            arr[-1] += x
        return x

    def increment(self, k: int, val: int) -> None:
        arr = self.arr
        n = len(arr)
        if n == 0:
            return
        k = min(k, n)
        arr[k - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)