# https://leetcode.com/problems/rearrange-words-in-a-sentence/
class Solution:
    def arrangeWords(self, text: str) -> str:
        a = [(len(w), i, w) for i, w in enumerate(text.lower().split())]
        a.sort()

        a1 = [x[2] for x in a]
        a1[0] = a1[0].capitalize()

        return ' '.join(a1)
