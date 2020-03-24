# https://leetcode.com/problems/reorder-data-in-log-files/
import re

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        al = []
        ad = []
        for s in logs:
            iden, log = s.split(None, 1)
            if re.match('[a-z ]+', log):
                al.append((log, iden, s))
            elif re.match('[0-9 ]+', log):
                ad.append(s)
        al.sort(key=lambda x: (x[0], x[1]))
        al = list(map(lambda x: x[2], al))
        return al + ad
