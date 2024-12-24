# easy
# https://leetcode.com/problems/count-days-spent-together/
class Solution:
    MD = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self) -> None:
        self.SUM_MD = [0]
        for x in self.MD:
            self.SUM_MD.append(self.SUM_MD[-1] + x)

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start_alice = self.getMonthDays(arriveAlice)
        end_alice = self.getMonthDays(leaveAlice) + 1
        start_bob = self.getMonthDays(arriveBob)
        end_bob = self.getMonthDays(leaveBob) + 1

        return max(0, min(end_alice, end_bob) - max(start_alice, start_bob))

    def getMonthDays(self, date_str):
        month = int(date_str[:2])
        day = int(date_str[3:5])
        return self.SUM_MD[month - 1] + day - 1
