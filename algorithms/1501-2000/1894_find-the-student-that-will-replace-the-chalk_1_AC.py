# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm = sum(chalk)
        k %= sm

        i = 0
        while True:
            if k < chalk[i]:
                break
            k -= chalk[i]
            i += 1
        return i
