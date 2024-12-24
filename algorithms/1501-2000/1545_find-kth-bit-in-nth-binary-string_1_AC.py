# medium
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
# much easier just to recur

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recur(n, k):
            if n == 1:
                return 0

            cur_len = (1 << n) - 1
            next_len = (1 << n - 1) - 1

            if k == next_len + 1:
                return 1

            if k <= next_len:
                return recur(n - 1, k)
            else:
                return 1 - recur(n - 1, 2 * (next_len + 1) - k)

        return str(recur(n, k))
