// Standard BFS
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::queue;
using std::string;
using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict;
        
        string start = beginWord;
        string end = endWord;
        
        dict.insert(start);
        
        int n = wordList.size();
        int i;
        for (i = 0; i < n; ++i) {
            dict.insert(wordList[i]);
        }
        if (dict.find(end) == dict.end()) {
            dict.clear();
            return 0;
        }
        
        unordered_map<string, int> ladder_len;
        queue<string> q;
        
        ladder_len[start] = 1;
        q.push(start);
        
        string s, s1;
        char ch;
        int ls;
        int j;
        while (!q.empty() && ladder_len.find(end) == ladder_len.end()) {
            s = q.front();
            q.pop();
            
            ls = s.size();
            s1 = s;
            for (i = 0; i < ls; ++i) {
                ch = s1[i];
                for (j = 0; j < 26; ++j) {
                    if (j + 'a' == ch) {
                        continue;
                    }
                    s1[i] = j + 'a';
                    if (dict.find(s1) == dict.end()) {
                        continue;
                    }
                    if (ladder_len.find(s1) != ladder_len.end()) {
                        continue;
                    }
                    ladder_len[s1] = ladder_len[s] + 1;
                    q.push(s1);
                }
                s1[i] = ch;
            }
        }
        int res = ladder_len.find(end) != ladder_len.end() ? ladder_len[end] : 0;
        
        dict.clear();
        ladder_len.clear();
        while (!q.empty()) {
            q.pop();
        }
        
        return res;
    }
};
