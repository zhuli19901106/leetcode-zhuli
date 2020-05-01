# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1179/
# 1AC
class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mm = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        mm = self.mm
        n = number
        if n in mm:
            mm[n] += 1
        else:
            mm[n] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        mm = self.mm
        for k, v in mm.items():
            if value - k == k and v > 1:
                return True
            elif value - k != k and value - k in mm:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)