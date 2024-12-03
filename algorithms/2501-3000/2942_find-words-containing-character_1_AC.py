# https://leetcode.com/problems/find-words-containing-character/
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i in range(len(words)) if x in words[i]]
