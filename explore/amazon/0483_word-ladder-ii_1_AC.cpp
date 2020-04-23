// Bidirectional BFS
#include <string>
#include <unordered_set>
#include <vector>
using std::string;
using std::unordered_set;
using std::vector;

class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        vector<vector<string>> res;
        string start = beginWord;
        string end = endWord;
        
        unordered_set<string> dict;
        int n = wordList.size();
        int i;
        for (i = 0; i < n; ++i) {
            dict.insert(wordList[i]);
        }
        dict.insert(start);
        
        if (dict.find(end) == dict.end()) {
            dict.clear();
            return res;
        }
        
        vector<unordered_set<string>> v1(1), v2(1);
        unordered_set<string> mark1, mark2;
        
        v1[0].insert(start);
        mark1.insert(start);
        v2[0].insert(end);
        mark2.insert(end);
        bool fail = false;
        while (!fail) {
            nextLevel(v1, mark1, dict);
            if (v1.back().size() == 0) {
                fail = true;
                break;
            }
            if (hasIntersect(v1.back(), v2.back())) {
                mergeSets(v1.back(), v2.back());
                v2.pop_back();
                break;
            }
            nextLevel(v2, mark2, dict);
            if (v2.back().size() == 0) {
                fail = true;
                break;
            }
            if (hasIntersect(v1.back(), v2.back())) {
                mergeSets(v1.back(), v2.back());
                v2.pop_back();
                break;
            }
        }
        
        if (!fail) {
            while (v2.size() > 0) {
                v1.push_back(v2.back());
                v2.pop_back();
            }
            v1.back().clear();
			v1.back().insert(end);
            
            vector<string> v;
            v.push_back(start);
            dfs(v, res, v1);
            v.pop_back();
        }
        
        dict.clear();
        v1.clear();
        v2.clear();
        mark1.clear();
        mark2.clear();
        
        return res;
    }
private:
    void nextLevel(vector<unordered_set<string>> &level, 
        unordered_set<string> &mark, unordered_set<string> &dict) {
        level.push_back(unordered_set<string>());
        auto &us1 = level.at(level.size() - 2);
        auto &us2 = level.at(level.size() - 1);
        
        string s;
        char ch;
        int i, j;
        int ls;
        for (auto it = us1.begin(); it != us1.end(); ++it) {
            s = *it;
            ls = s.size();
            for (i = 0; i < ls; ++i) {
                ch = s[i];
                for (j = 0; j < 26; ++j) {
                    s[i] = j + 'a';
                    if (j + 'a' == ch || dict.find(s) == dict.end() || 
                        mark.find(s) != mark.end()) {
                        continue;
                    }
                    us2.insert(s);
                    mark.insert(s);
                }
                s[i] = ch;
            }
        }
    }
    
    bool hasIntersect(unordered_set<string> &us1, unordered_set<string> &us2) {
        for (auto it = us1.begin(); it != us1.end(); ++it) {
            if (us2.find(*it) != us2.end()) {
                return true;
            }
        }
        return false;
    }
    
    void mergeSets(unordered_set<string> &us1, unordered_set<string> &us2) {
        for (auto it = us2.begin(); it != us2.end(); ++it) {
            if (us1.find(*it) == us1.end()) {
                us1.insert(*it);
            }
        }
    }
    
    void dfs(vector<string> &v, vector<vector<string>> &res, 
        vector<unordered_set<string>> &level) {
        if (v.size() == level.size()) {
            res.push_back(v);
            return;
        }
        
        string s = v.back();
        char ch;
        int i, j;
        int ls = s.size();
        int idx = v.size();
        
        for (i = 0; i < ls; ++i) {
            ch = s[i];
            for (j = 0; j < 26; ++j) {
                s[i] = j + 'a';
                if (j + 'a' == ch || level[idx].find(s) == level[idx].end()) {
                    continue;
                }
                v.push_back(s);
                dfs(v, res, level);
                v.pop_back();
            }
            s[i] = ch;
        }
    }
};
