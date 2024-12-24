# medium
# https://leetcode.com/problems/design-circular-queue/
# so you expect this done within 5 minutes?
# I don't think so.
class MyCircularQueue:
    NULL_VAL = -1

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.cap = k
        self.arr = [0 for i in range(k + 1)]
        self.size = 0
        self.head = 0
        self.tail = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.head] = value
        self.head = (self.head + 1) % (self.cap + 1)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % (self.cap + 1)
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return MyCircularQueue.NULL_VAL
        return self.arr[(self.tail + 1) % (self.cap + 1)]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return MyCircularQueue.NULL_VAL
        return self.arr[(self.head + self.cap) % (self.cap + 1)]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()