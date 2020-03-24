#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        vector<string> vt;
        int nt;
        int i;
        string path, fname, content;
        unordered_map<string, vector<string>> um;
        
        for (string &s: paths) {
            tokenize(s, vt);
            nt = vt.size();
            path = vt[0];
            for (i = 1; i < nt; ++i) {
                parse(vt[i], fname, content);
                um[content].push_back(path + "/" + fname);
            }
        }
        
        vector<vector<string>> res;
        for (auto it = um.begin(); it != um.end(); ++it) {
            if (it->second.size() > 1) {
                res.push_back(it->second);
            }
        }
        um.clear();
        
        return res;
    }
private:
    void tokenize(const string &s, vector<string> &vt) {
        int ls = s.size();
        int cnt_br = 0;
        int i = 0;
        
        string ss = "";
        vt.clear();
        while (true) {
            while (i < ls && s[i] == ' ' && cnt_br == 0) {
                ++i;
            }
            if (i >= ls) {
                break;
            }
            
            while (i < ls) {
                if (cnt_br == 0 && s[i] == ' ') {
                    break;
                }
                if (s[i] == '(') {
                    ++cnt_br;
                } else if (s[i] == ')') {
                    --cnt_br;
                }
                ss.push_back(s[i]);
                ++i;
            }
            vt.push_back(ss);
            ss.clear();
            if (i >= ls) {
                break;
            }
        }
    }
    
    void parse(const string &s, string &fname, string &content) {
        int ls = s.size();
        int i;
        
        fname = "";
        content = "";
        i = 0;
        while (s[i] != '(') {
            fname.push_back(s[i++]);
        }
        ++i;
        while (s[i] != ')') {
            content.push_back(s[i++]);
        }
    }
};
