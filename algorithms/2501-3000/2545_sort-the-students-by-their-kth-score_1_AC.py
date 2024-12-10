# https://leetcode.com/problems/sort-the-students-by-their-kth-score/
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(score), len(score[0])
        ak = [(score[i][k], i) for i in range(n)]
        ak.sort(reverse=True)

        res = []
        for i in range(n):
            res.append(score[ak[i][1]][:])
        return res
