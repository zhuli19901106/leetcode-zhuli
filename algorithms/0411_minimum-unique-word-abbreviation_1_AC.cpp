// I tried to write an iterative version, but it didn't work.
// Had to make do with DFS after all.
// The idea of bit masking is clever.
#include <string>
#include <unordered_set>
#include <vector>
using std::string;
using std::to_string;
using std::unordered_set;
using std::vector;

class Solution {
public:
    string minAbbreviation(string target, vector<string>& dictionary) {
        string &s = target;
        int ls = s.size();
        int max_bt = (1 << ls);
        
        unordered_set<int> us;
        int bt;
        int lt;
        int i;
        for (string &t: dictionary) {
            bt = 0;
            lt = t.size();
            if (ls != lt) {
                continue;
            }
            bt = 0;
            for (i = 0; i < ls; ++i) {
                if (s[i] == t[i]) {
                    bt |= (1 << i);
                }
            }
            markBit(us, bt);
        }
		if (us.size() == 0) {
			return to_string(ls);
		}
        
        string res = s;
        dfs(1, 0, 0, 0, s, us, res);
        dfs(2, 0, 0, 0, s, us, res);
        us.clear();
        
        return res;
    }
private:
    void dfs(int type, int idx, int len, int bt, string &s, 
        unordered_set<int> &us, string &res) {
        // Pruning here
        if (len >= res.size()) {
            return;
        }
        
        int ls = s.size();
        if (idx == ls) {
            if (us.find(bt) == us.end()) {
                res = bitToString(s, bt);
            }
            return;
        }
        
        int next_len;
        int next_bt;
        int i, j;
        for (i = ls; i > idx; --i) {
            next_bt = bt;
            if (type == 1) {
                next_len = len + 1;
            } else {
                next_len = len + i - idx;
                for (j = idx; j < i; ++j) {
                    next_bt |= (1 << j);
                }
            }
            dfs(3 - type, i, next_len, next_bt, s, us, res);
        }
    }
    
    void markBit(unordered_set<int> &us, int bt) {
        if (us.find(bt) != us.end()) {
            return;
        }
        us.insert(bt);
        
        int i = 1;
        while (i <= bt) {
            if (bt & i) {
                markBit(us, bt ^ i);
            }
			i <<= 1;
        }
    }
    
    string bitToString(string &s, int bt) {
        string res = "";
        int last_i = -1;
        int i;
        for (i = 0; (1 << i) <= bt; ++i) {
            if ((bt & (1 << i)) == 0) {
                continue;
            }
            if (i - 1 > last_i) {
                res += to_string(i - 1 - last_i);
            }
            res.push_back(s[i]);
            last_i = i;
        }
        
        int ls = s.size();
        if (ls - 1 > last_i) {
            res += to_string(ls - 1 - last_i);
        }
        
        return res;
    }
};
