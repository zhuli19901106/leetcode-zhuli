# https://leetcode.com/problems/goal-parser-interpretation/
# 1AC
import re

class Solution:
    def interpret(self, command: str) -> str:
        s = command
        s = re.sub('\(\)', 'o', s)
        s = re.sub('\(al\)', 'al', s)
        return s
