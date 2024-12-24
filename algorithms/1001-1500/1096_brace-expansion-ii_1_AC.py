# hard
# https://leetcode.com/problems/brace-expansion-ii/
# damn...that's better

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # split tokens
        s = expression
        n = len(s)
        tks = []
        i = 0
        while i < n:
            if not s[i].isalpha():
                tks.append(s[i])
                i += 1
                continue
            cur = []
            while i < n and s[i].isalpha():
                cur.append(s[i])
                i += 1
            tks.append(''.join(cur))

        # add special op
        tks1 = []
        nt = len(tks)
        for i, tk in enumerate(tks):
            tks1.append(tk)
            if i == nt - 1:
                continue
            if (tk == '}' and tks[i + 1].isalpha()) or \
                (tk.isalpha() and tks[i + 1] == '{') or \
                (tk == '}' and tks[i + 1] == '{'):
                tks1.append('*')

        tks = tks1
        nt = len(tks)

        def calc(ve, vo):
            if len(ve) < 2 or len(vo) < 1:
                return
            e2 = ve.pop()
            e1 = ve.pop()
            op = vo.pop()
            if op == ',':
                e3 = e1 | e2
            elif op == '*':
                e3 = set()
                for x in e1:
                    for y in e2:
                        e3.add(x + y)
            ve.append(e3)

        # make a calculator
        pred = {
            '{': -1,
            ',': 1,
            '*': 2,
        }

        ve, vo = [], []
        for tk in tks:
            if tk == ',' or tk == '*':
                while len(vo) > 0 and pred[vo[-1]] >= pred[tk]:
                    calc(ve, vo)
                vo.append(tk)
            elif tk == '{':
                vo.append(tk)
            elif tk == '}':
                while vo[-1] != '{':
                    calc(ve, vo)
                vo.pop()
            elif tk.isalpha():
                ve.append(set([tk]))
            else:
                pass
        while len(vo) > 0:
            calc(ve, vo)

        return sorted(ve.pop())
