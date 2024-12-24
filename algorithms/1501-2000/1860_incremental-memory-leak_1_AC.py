# medium
# https://leetcode.com/problems/incremental-memory-leak/
# 1AC, pure simulation

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while True:
            if max(memory1, memory2) < i:
                break
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1
        return i, memory1, memory2
