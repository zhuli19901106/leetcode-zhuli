# https://leetcode.com/problems/maximum-score-from-removing-stones/
# just simulate
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [a, b, c]
        arr.sort()
        if arr[0] + arr[1] <= arr[2]:
            return arr[0] + arr[1]

        res = 0
        res += arr[1] - arr[0]
        arr[2] -= arr[1] - arr[0]
        arr[1] = arr[0]

        res += arr[2]
        arr[0] -= arr[2] // 2
        arr[1] -= (arr[2] + 1) // 2
        arr[2] = 0
        res += arr[1]

        return res
