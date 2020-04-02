# https://leetcode.com/problems/web-crawler/
# 1AC, BFS
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import re
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def getHost(url):
            m = re.match(r'^http://(.*?)(/.*)?$', url)
            return m.group(1)

        st = set()
        q = deque()

        host = getHost(startUrl)

        st.add(startUrl)
        q.append(startUrl)
        while len(q) > 0:
            url = q.popleft()
            urls = htmlParser.getUrls(url)
            for url1 in urls:
                host1 = getHost(url1)
                if host1 != host or url1 in st:
                    continue
                st.add(url1)
                q.append(url1)

        res = list(st)
        res.sort()
        return res
