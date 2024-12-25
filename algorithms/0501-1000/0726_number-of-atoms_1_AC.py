# hard
# https://leetcode.com/problems/number-of-atoms/
# parser, again
# the formula is assumed to be valid
# just be patient
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        tks = self.tokenize(formula)
        nt = len(tks)

        st = [{}]
        i = 0
        elem = None
        while i < nt:
            tk = tks[i]
            next_tk = (tks[i + 1] if i < nt - 1 else None)

            # left bracket
            if tk == '(':
                st.append({})
                i += 1
            # right bracket
            elif tk == ')':
                mm_pop = st.pop()
                mm = st[-1]

                mult = 1
                if type(next_tk) == int:
                    mult = next_tk
                    i += 2
                else:
                    i += 1

                for x in mm_pop:
                    if not x in mm:
                        mm[x] = 0
                    mm[x] += mm_pop[x] * mult
            # count
            elif type(tk) == int:
                # actually shouldn't be here
                i += 1
            # element name
            else:
                mult = 1
                if type(next_tk) == int:
                    mult = next_tk
                    i += 2
                else:
                    i += 1

                mm = st[-1]
                if not tk in mm:
                    mm[tk] = 0
                mm[tk] += mult

        if len(st) != 1:
            return ''

        res = []
        mm = st.pop()
        for x in sorted(mm.keys()):
            res.append(f'{x}{mm[x]}' if mm[x] > 1 else f'{x}')
        res = ''.join(res)
        return res

    def tokenize(self, formula):
        # tokenize
        tks = []

        s = formula
        ns = len(s)
        i = 0
        while i < ns:
            if s[i] in '()':
                tks.append(s[i])
                i += 1
                continue

            if s[i].isupper():
                j = i + 1
                while j < ns and s[j].islower():
                    j += 1
                tks.append(s[i: j])
                i = j
                continue

            if s[i].isdigit():
                j = i + 1
                while j < ns and s[j].isdigit():
                    j += 1
                tks.append(int(s[i: j]))
                i = j
                continue

            # maybe invalid
            i += 1

        return tks
