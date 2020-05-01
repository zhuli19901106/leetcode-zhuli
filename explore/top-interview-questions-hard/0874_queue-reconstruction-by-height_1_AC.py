# https://leetcode.com/explore/interview/card/top-interview-questions-hard/124/others/874/
# that's a clever solution
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ap = people
        ap.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for h, i in ap:
            res.insert(i, [h, i])
        return res
