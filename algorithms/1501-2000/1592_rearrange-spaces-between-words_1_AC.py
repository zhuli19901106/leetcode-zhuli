# easy
# https://leetcode.com/problems/rearrange-spaces-between-words/
# watch for the edge case
import re

class Solution:
    def reorderSpaces(self, text: str) -> str:
        ws = text.strip().split()
        nw = len(ws)
        ns = len(re.sub(r'\S', '', text))

        sep = ' ' * (ns // (nw - 1)) if nw > 1 else ''
        tail = ' ' * (ns - len(sep) * (nw - 1))
        return sep.join(ws) + tail
