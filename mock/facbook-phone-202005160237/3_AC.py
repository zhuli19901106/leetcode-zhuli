class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if len(num) == 0:
            return []

        ops = {}
        ops['+'] = lambda x, y: x + y
        ops['-'] = lambda x, y: x - y
        ops['*'] = lambda x, y: x * y

        res = []
        def dfs(idx, arr, op):
            nonlocal res

            if idx == len(num):
                expr = ''.join(arr)
                n = eval(expr)
                if n == target:
                    res.append(expr)
                return
            if op:
                for c in ops:
                    arr.append(c)
                    dfs(idx, arr, not op)
                    arr.pop()
            else:
                nr = len(num) if num[idx] != '0' else idx + 1
                for i in range(idx, nr):
                    x = num[idx: i + 1]
                    arr.append(x)
                    dfs(i + 1, arr, not op)
                    arr.pop()
        dfs(0, [], False)
        return res
