# https://leetcode.com/problems/masking-personal-information/
# that's violation of the single responsibility rule, you know?
import re

class Solution:
    def maskPII(self, S: str) -> str:
        s = S
        pat = r'(\w+)@(\w+)\.(\w+)'
        m = re.match(pat, s)
        if m:
            gs = [x.lower() for x in m.groups()]
            n = len(gs[0])
            if n >= 2:
                gs[0] = gs[0][0] + ('*' * 5) + gs[0][-1]
            return f'{gs[0]}@{gs[1]}.{gs[2]}'

        s = re.sub(r'\D', '', s)
        n = len(s)
        cc = '+{}-'.format('*' * (n - 10)) if n > 10 else ''
        return f'{cc}***-***-{s[-4:]}'
