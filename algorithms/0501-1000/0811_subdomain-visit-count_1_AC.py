# medium
# https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        m = {}
        for record in cpdomains:
            cnt, url = record.split(' ')
            cnt = int(cnt)
            tokens = url.split('.')
            n = len(tokens)
            s = ''
            for i in range(n - 1, -1, -1):
                s = '{}{}{}'.format(tokens[i], '' if i == n - 1 else '.', s)
                if not s in m:
                    m[s] = 0
                m[s] += cnt
        res = [f'{v} {k}' for k, v in m.items()]
        return res
