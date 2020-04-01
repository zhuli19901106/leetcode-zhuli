# https://leetcode.com/problems/word-frequency/
# Read from the file words.txt and output the word frequency list to stdout.
# I hate regex
cat words.txt | sed 's/^\s\+//g' | sed 's/\s\+$//g' | sed 's/\s\+/ /g' | tr ' ' '\n' | sort | uniq -c | sort -n -r -k 1 | awk '{print $2" "$1}'
