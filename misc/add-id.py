#!/usr/bin/env python
from bs4 import BeautifulSoup
from glob import glob
import re
import shutil

def process_row(r):
    a = r.find('a')
    a_attr = a.attrs
    url = a_attr['href']
    pref = re.match(r'/problems/(.*)', url).group(1)
    pid = int(r.find_all('td')[1].contents[0])
    mm = {}
    mm['pref'] = pref
    mm['pid'] = pid
    return mm

def main():
    fns = glob('*.cpp') + glob('*.py') + glob('*.sql')
    mfn = {}
    # extract file prefix from glob
    for fn in fns:
        m = re.match(r'^([a-z0-9\-]+).*', fn)
        pref = m.group(1)
        if not pref in mfn:
            mfn[pref] = []
        mfn[pref].append(fn)

    # extract problem id from html
    html_str = ''
    with open('./leetcode-problem-list.html', 'r') as f:
        html_str = f.read()
    html = BeautifulSoup(html_str, 'html.parser')
    tbody = html.find('tbody', attrs={'class': 'reactable-data'})
    rs = tbody.find_all('tr')
    row_infos = [process_row(r) for r in rs]

    mid = {}
    for row_info in row_infos:
        mid[row_info['pref']] = row_info['pid']

    for pref in mfn:
        for fn in mfn[pref]:
            pid = '{:04d}'.format(mid[pref])
            fn1 = 'done/{}_{}'.format(pid, fn)
            print(fn1)
            shutil.move(fn, fn1)

if __name__ == '__main__':
    main()
