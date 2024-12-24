# medium
# https://leetcode.com/problems/reordered-power-of-2/
class Solution:
    def __init__(self):
        self.st2 = set()
        for i in range(31):
            self.st2.add(''.join(sorted(str(2 ** i))))

    def reorderedPowerOf2(self, N: int) -> bool:
        return ''.join(sorted(str(N))) in self.st2
