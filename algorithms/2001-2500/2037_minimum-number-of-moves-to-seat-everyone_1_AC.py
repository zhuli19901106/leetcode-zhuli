# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
# 1AC, what if seats are at the same position?

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        arr_seat = sorted(seats)
        arr_stud = sorted(students)
        n = len(arr_seat)
        res = 0
        for i in range(n):
            res += abs(arr_seat[i] - arr_stud[i])
        return res
