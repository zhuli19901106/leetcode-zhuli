# medium
# https://leetcode.com/problems/design-circular-deque/
# man... that's overwork
class MyCircularDeque:
    NULL_VAL = -1

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k
        self.arr = [0 for i in range(k + 1)]
        self.size = 0
        self.head = 0
        self.tail = k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.head] = value
        self.head = (self.head + 1) % (self.cap + 1)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.tail] = value
        self.tail = (self.tail + self.cap) % (self.cap + 1)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.head = (self.head + self.cap) % (self.cap + 1)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % (self.cap + 1)
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return MyCircularDeque.NULL_VAL
        return self.arr[(self.head + self.cap) % (self.cap + 1)]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return MyCircularDeque.NULL_VAL
        return self.arr[(self.tail + 1) % (self.cap + 1)]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.cap

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()