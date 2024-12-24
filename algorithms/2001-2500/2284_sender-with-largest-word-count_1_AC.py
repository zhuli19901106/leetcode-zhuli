# medium
# https://leetcode.com/problems/sender-with-largest-word-count/
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mm = {}
        ac = [len(s.strip().split()) for s in messages]
        n = len(ac)
        for i in range(n):
            if senders[i] in mm:
                mm[senders[i]] += ac[i]
            else:
                mm[senders[i]] = ac[i]

        max_name, max_cnt = '', -1
        for name, cnt in mm.items():
            if cnt > max_cnt or (cnt == max_cnt and name > max_name):
                max_name, max_cnt = name, cnt

        return max_name
