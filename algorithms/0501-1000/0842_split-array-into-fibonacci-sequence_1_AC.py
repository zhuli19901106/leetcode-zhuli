# medium
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# DFS solution, careful with the data range
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        INT_MAX = 2 ** 31 - 1

        a = [ord(c) - ord('0') for c in S]
        n = len(a)
        res = None

        def dfs(idx, seq):
            nonlocal res

            if res:
                return

            ns = len(seq)

            if idx == n:
                if ns >= 3:
                    res = seq[:]
                return

            i = idx
            val = 0
            while i < n:
                val = val * 10 + a[i]
                i += 1
                if val > INT_MAX:
                    break

                if ns < 2 or seq[-2] + seq[-1] == val:
                    seq.append(val)
                    dfs(i, seq)
                    seq.pop()
                if a[idx] == 0:
                    break
                if ns >= 3 and seq[-2] + seq[-1] < val:
                    break

        dfs(0, [])
        return res if res else []
