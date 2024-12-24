# easy
# https://leetcode.com/problems/capitalize-the-title/
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def process(w):
            return w.lower() if len(w) <= 2 else w[0].upper() + w[1:].lower()

        return ' '.join(map(process, title.split()))
