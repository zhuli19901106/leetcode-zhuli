# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def getMinutes(s):
            return int(s[:2]) * 60 + int(s[3:])

        diff = getMinutes(correct) - getMinutes(current)
        return diff // 60 + diff % 60 // 15 + diff % 15 // 5 + diff % 5
