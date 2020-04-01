# https://leetcode.com/problems/tenth-line/
# Read from the file file.txt and output the tenth line to stdout.
cat file.txt | tail -n +10 | head -n 1
