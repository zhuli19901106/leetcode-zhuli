# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
# 1AC
import re

class Solution:
    def removeVowels(self, S: str) -> str:
        return re.sub('[aeiou]', '', S)
