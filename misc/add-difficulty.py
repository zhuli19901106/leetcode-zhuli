#!/usr/bin/python3
'''
a one-time script to add difficulty marker for all solved algorithm problems.
problem list is extracted from the graphql API on LeetCode.
'''
import json
import logging
import os

logging.basicConfig(level=logging.WARN)
log = logging.getLogger(__name__)

NUM_PER_DIR = 500

def main():
    with open('data.json', 'r') as inf:
        data = json.load(inf)
    questions = data['data']['problemsetQuestionList']['questions']

    skipped = []
    processed = []
    missing = []

    for q in questions:
        found = False
        qid = int(q['frontendQuestionId'])
        qid_str = q['frontendQuestionId'].zfill(4)
        difficulty = q['difficulty'].lower()
        slug = q['titleSlug']
        title = q['title']

        qid_low = (qid - 1) // NUM_PER_DIR * NUM_PER_DIR + 1
        qid_high = qid_low - 1 + NUM_PER_DIR
        dir_name = f'../algorithms/{qid_low:04d}-{qid_high:04d}'
        for i in range(1, 4):
            for suf in ['cpp', 'py']:
                full_name = os.path.abspath(f'{dir_name}/{qid_str}_{slug}_{i}_AC.{suf}')
                base_name = os.path.basename(full_name)
                if os.path.isfile(full_name):
                    found = True

                    log.info('found %s file %s', suf, full_name)
                    if checkDifficulty(full_name, difficulty):
                        skipped.append(f'{os.path.basename(full_name)}')
                        log.info('file %s skipped', base_name)
                        continue

                    addDifficulty(full_name, difficulty)
                    processed.append(f'{os.path.basename(full_name)}')
                    log.info('file %s processed', base_name)

        if not found:
            log.warn('file for question %s %s is not found', qid_str, title)

def checkDifficulty(file_name, difficulty):
    if file_name.endswith('.cpp'):
        comment = '// {}'
    elif file_name.endswith('.py'):
        comment = '# {}'

    lines = []
    with open(file_name, 'r', encoding='utf-8') as inf:
        lines = inf.readlines()

    comment = comment.format(difficulty)
    if len(lines) > 0 and lines[0] == comment + '\n':
        log.info('searching %s for "%s", found "%s"', os.path.basename(file_name), \
            comment, lines[0].strip())
        return True
    else:
        return False

def addDifficulty(file_name, difficulty):
    if file_name.endswith('.cpp'):
        comment = '// {}'
    elif file_name.endswith('.py'):
        comment = '# {}'

    with open(file_name, 'r', encoding='utf-8') as inf:
        s = inf.read()

    comment = comment.format(difficulty)
    s = comment + '\n' + s

    with open(file_name, 'w', encoding='utf-8') as outf:
        outf.write(s)

    log.info('added comment "%s" to file %s', comment, os.path.basename(file_name))

if __name__ == '__main__':
    main()

'''
these problems have changed titles or wrong file names, fixed by hand
- WARNING:__main__:file for question 0028 Find the Index of the First Occurrence in a String is not found
- WARNING:__main__:file for question 0211 Design Add and Search Words Data Structure is not found
- WARNING:__main__:file for question 0491 Non-decreasing Subsequences is not found
- WARNING:__main__:file for question 0518 Coin Change II is not found
- WARNING:__main__:file for question 0547 Number of Provinces is not found
- WARNING:__main__:file for question 0561 Array Partition is not found
- WARNING:__main__:file for question 0755 Pour Water is not found
- WARNING:__main__:file for question 1027 Longest Arithmetic Subsequence is not found
- WARNING:__main__:file for question 1217 Minimum Cost to Move Chips to The Same Position is not found
- WARNING:__main__:file for question 1375 Number of Times Binary String Is Prefix-Aligned is not found
- WARNING:__main__:file for question 1430 Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree is not found
- WARNING:__main__:file for question 1460 Make Two Arrays Equal by Reversing Subarrays is not found
- WARNING:__main__:file for question 1529 Minimum Suffix Flips is not found
- WARNING:__main__:file for question 1578 Minimum Time to Make Rope Colorful is not found
- WARNING:__main__:file for question 1688 Count of Matches in Tournament is not found
- WARNING:__main__:file for question 1954 Minimum Garden Perimeter to Collect Enough Apples is not found
- WARNING:__main__:file for question 2350 Shortest Impossible Sequence of Rolls is not found
- WARNING:__main__:file for question 2549 Count Distinct Numbers on Board is not found
- WARNING:__main__:file for question 2807 Insert Greatest Common Divisors in Linked List is not found
- WARNING:__main__:file for question 2914 Minimum Number of Changes to Make Binary String Beautiful is not found
- WARNING:__main__:file for question 3285 Find Indices of Stable Mountains is not found
- WARNING:__main__:file for question 3318 Find X-Sum of All K-Long Subarrays I is not found
'''
