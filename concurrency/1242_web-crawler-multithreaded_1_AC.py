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
# 1AC, this problem can be expanded into a full-scale industrial project
from threading import Lock, Thread
from urllib.parse import urlparse

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        lk = Lock()
        st = set()
        host = urlparse(startUrl).hostname

        def worker(url0):
            urls = htmlParser.getUrls(url0)
            ths = []
            
            # you know, this is basically synchronized
            with lk:
                for url in urls:
                    if url in st:
                        continue
                    cur_host = urlparse(url).hostname
                    if cur_host != host:
                        continue

                    st.add(url)
                    ths.append(Thread(target=worker, args=(url,)))
            for th in ths:
                th.start()
            for th in ths:
                th.join()

        st.add(startUrl)
        # the comma in args is needed
        th = Thread(target=worker, args=(startUrl,))
        th.start()
        th.join()
        return list(st)
