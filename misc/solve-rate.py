#!/usr/bin/python3
'''
a misc script to count completion rates for every hundred problems
'''
import glob
import logging
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def get_solve_list():
    base_dir = os.path.abspath(os.path.realpath(__file__) + '/../../algorithms/')
    os.chdir(base_dir)

    solve_ids = set()

    algo_dirs = os.listdir(base_dir)
    for algo_dir in algo_dirs:
        os.chdir(algo_dir)
        filenames = glob.glob('*.cpp') + glob.glob('*.py')
        solve_ids |= set([int(fn[:4]) for fn in filenames])
        os.chdir('..')
    solve_ids = sorted(solve_ids)

    return solve_ids

def count_solve_rate(solve_ids):
    stats = {}

    n = len(solve_ids)
    i = 0
    ll = 1
    while True:
        rr = ll + 99
        key = f'{ll:4d}-{rr:4d}'

        j = i
        while j < n and solve_ids[j] <= rr:
            j += 1
        if j == i:
            break
        stats[key] = (j - i) / 100.0
        i = j

        ll += 100

    for key, val in stats.items():
        log.info('%s: %.2f%%', key, val * 100.0)

def main():
    solve_ids = get_solve_list()
    count_solve_rate(solve_ids)

if __name__ == '__main__':
    main()

'''
INFO:__main__:   1- 100: 100.00%
INFO:__main__: 101- 200: 84.00%
INFO:__main__: 201- 300: 99.00%
INFO:__main__: 301- 400: 100.00%
INFO:__main__: 401- 500: 99.00%
INFO:__main__: 501- 600: 82.00%
INFO:__main__: 601- 700: 75.00%
INFO:__main__: 701- 800: 83.00%
INFO:__main__: 801- 900: 82.00%
INFO:__main__: 901-1000: 79.00%
INFO:__main__:1001-1100: 78.00%
INFO:__main__:1101-1200: 60.00%
INFO:__main__:1201-1300: 67.00%
INFO:__main__:1301-1400: 65.00%
INFO:__main__:1401-1500: 66.00%
INFO:__main__:1501-1600: 48.00%
INFO:__main__:1601-1700: 52.00%
INFO:__main__:1701-1800: 49.00%
INFO:__main__:1801-1900: 44.00%
INFO:__main__:1901-2000: 42.00%
INFO:__main__:2001-2100: 48.00%
INFO:__main__:2101-2200: 47.00%
INFO:__main__:2201-2300: 41.00%
INFO:__main__:2301-2400: 41.00%
INFO:__main__:2401-2500: 47.00%
INFO:__main__:2501-2600: 45.00%
INFO:__main__:2601-2700: 30.00%
INFO:__main__:2701-2800: 28.00%
INFO:__main__:2801-2900: 26.00%
INFO:__main__:2901-3000: 34.00%
INFO:__main__:3001-3100: 31.00%
INFO:__main__:3101-3200: 31.00%
INFO:__main__:3201-3300: 29.00%
INFO:__main__:3301-3400: 20.00%
'''
