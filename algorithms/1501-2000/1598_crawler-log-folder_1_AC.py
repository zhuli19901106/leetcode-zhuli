# https://leetcode.com/problems/crawler-log-folder/
# 1AC
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for op in logs:
            if op == './':
                continue
            elif op == '../':
                cnt = max(0, cnt - 1)
            else:
                cnt += 1
        return cnt
