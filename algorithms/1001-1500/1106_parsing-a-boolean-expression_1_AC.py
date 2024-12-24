# hard
# https://leetcode.com/problems/parsing-a-boolean-expression/
# right..., a parser
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops, vals = [], []

        s = expression
        n = len(s)
        i = 0
        # invalid expressions are not handled
        while i < n:
            print(f'i = {i} s[i] = {s[i]} ops = {ops} vals = {vals}')
            if s[i] == ',':
                i += 1
                continue

            if s[i] in 'tf':
                vals.append((True if s[i] == 't' else False, len(ops)))
                i += 1
                continue

            if s[i] in '!&|':
                if i == n - 1 or s[i + 1] != '(':
                    # invalid
                    return None
                ops.append(s[i])
                i += 2
                continue

            if s[i] != ')' or len(ops) == 0:
                return None

            cur_op = ops.pop()
            if cur_op == '!':
                val, idx = vals.pop()
                vals.append((not val, len(ops)))
            elif cur_op == '&':
                val_and = True
                while len(vals) > 0 and vals[-1][1] > len(ops):
                    val, idx = vals.pop()
                    val_and &= val
                vals.append((val_and, len(ops)))
            elif cur_op == '|':
                val_or = False
                while len(vals) > 0 and vals[-1][1] > len(ops):
                    val, idx = vals.pop()
                    val_or |= val
                vals.append((val_or, len(ops)))
            i += 1

        return vals[0][0] if (len(vals) == 1 and vals[0][1] == 0) else None
