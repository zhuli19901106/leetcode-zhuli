# https://leetcode.com/problems/unique-email-addresses/
import re

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        norm_emails = set()
        for em in emails:
            norm_emails.add(self.normalize(em))
        return len(norm_emails)

    def normalize(self, s):
        p = '(.*)(@.*)'
        m = re.match(p, s)
        g1 = m.group(1)
        g1 = re.sub('\.', '', g1)
        g1 = re.match('([\w\.]*)(\+[\w\+\.]*)?', g1).group(1)
        g2 = m.group(2)
        res = '{}{}'.format(g1, g2)
        return res
