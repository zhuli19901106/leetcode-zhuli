#!/usr/bin/env python3
# old url: https://github.com/zhuli19901106/leetcode-zhuli/blob/master/longest-substring-without-repeating-characters_1_AC.cpp
# new url: https://github.com/zhuli19901106/leetcode-zhuli/blob/master/algorithms/0001-0500/0003_longest-substring-without-repeating-characters_1_AC.cpp
import glob
import re
from bs4 import BeautifulSoup

input_fn = 'review.md'
path_pref = 'algorithms/0501-1000/'
new_url_pref = 'https://github.com/zhuli19901106/leetcode-zhuli/blob/master/'
problem_list_fn = 'leetcode-problem-list.html'
leetcode_url_pref = 'https://leetcode.com/problems/'

def process_url(s, file_dict):
    m = re.search(r'(.*)(https://github\.com/zhuli19901106/leetcode-2/blob/master/)(.*)$', s)
    if not m:
        return s
    text = m.group(1)
    url_pref = m.group(2)
    old_f = m.group(3)
    new_f = file_dict[old_f]
    return '{}{}{}{}\n'.format(text, new_url_pref, path_pref, new_f)

def process_description(s, ps_dict):
    m = re.search(r'^// #(\d+) (Description:.*)$', s)
    if not m:
        return s
    pid = int(m.group(1))
    url = '{}{}/'.format(leetcode_url_pref, ps_dict[pid])
    desc = m.group(2)
    return '// [#{}]({}) {}\n'.format(pid, url, desc)

def get_file_dict():
    fs = []
    for ext in ('py', 'cpp'):
        fs += glob.glob('*.{}'.format(ext))
    mf = {}
    for f in fs:
        m = re.match(r'\d+_(.*)', f)
        old_f = m.group(1)
        mf[old_f] = f
    return mf

def get_problem_info(r):
    a = r.find('a')
    a_attr = a.attrs
    url = a_attr['href']
    pref = re.match(r'/problems/(.*)', url).group(1)
    pid = int(r.find_all('td')[1].contents[0])
    mm = {}
    mm['pref'] = pref
    mm['pid'] = pid
    return mm

def get_ps_dict():
    # extract problem id from html
    html_str = ''
    with open(problem_list_fn, 'r') as f:
        html_str = f.read()
    html = BeautifulSoup(html_str, 'html.parser')
    tbody = html.find('tbody', attrs={'class': 'reactable-data'})
    rs = tbody.find_all('tr')
    row_infos = [get_problem_info(r) for r in rs]

    mm = {}
    for row_info in row_infos:
        mm[row_info['pid']] = row_info['pref']
    return mm

def main():
    file_dict = get_file_dict()
    ps_dict = get_ps_dict()

    with open(input_fn, 'r') as f:
        a0 = f.readlines()
    output_fn = '123'
    f = open(output_fn, 'w')

    a = a0[:]
    for i in range(len(a)):
        a[i] = process_url(a[i], file_dict)
        a[i] = process_description(a[i], ps_dict)
        print(a[i], end='')
        f.write(a[i])
    f.close()

if __name__ == '__main__':
    main()
