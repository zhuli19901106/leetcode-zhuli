# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:idx + 1][::-1] + word[idx + 1:]
