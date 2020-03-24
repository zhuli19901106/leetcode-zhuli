#include <string>
using std::to_string;

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<int> ip;
        vector<string> res;
        dfs(0, ip, s, res);
        
        return res;
    }
private:
    static const int R = 10;
    static const int IP_LEN = 4;
    
    void dfs(int idx, vector<int> &ip, string &s, vector<string> &res) {
        int val;
        int ls = s.size();
        if (ip.size() == IP_LEN) {
            if (idx < ls) {
                return;
            }
            string ip_s = to_string(ip[0]);
            int i;
            for (i = 1; i < IP_LEN; ++i) {
                ip_s += "." + to_string(ip[i]);
            }
            res.push_back(ip_s);
            return;
        }
        
        val = 0;
        while (idx < ls) {
            val = val * R + (s[idx++] - '0');
            if (val > 255) {
                break;
            }
            ip.push_back(val);
            dfs(idx, ip, s, res);
            ip.pop_back();
            if (val == 0) {
                // Leading zero
                break;
            }
        }
    }
};
