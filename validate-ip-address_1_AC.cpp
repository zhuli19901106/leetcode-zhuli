#include <cctype>
#include <cstdio>
using std::isupper;
using std::sscanf;
using std::tolower;

class Solution {
public:
    string validIPAddress(string IP) {
        int ls = IP.size();
        int cnt_dot = 0;
        int cnt_colon = 0;
        int i;
        for (i = 0; i < ls; ++i) {
            if (IP[i] == '.') {
                ++cnt_dot;
            }
            if (IP[i] == ':') {
                ++cnt_colon;
            }
        }
        
        if (cnt_colon == 0 && cnt_dot == 3 && validIPv4(IP)) {
            return "IPv4";
        }
        if (cnt_colon == 7 && cnt_dot == 0 && validIPv6(IP)) {
            return "IPv6";
        }
        return "Neither";
    }
private:
    bool validIPv4(string s) {
        int ls = s.size();
        int lss;
        int i, j, k;
        string ss;
        int val;
        int cnt;
        
        i = 0;
        cnt = 0;
        while (i < ls) {
            j = i;
            while (j < ls && s[j] != '.') {
                ss.push_back(s[j++]);
            }
            if (ss.size() == 0) {
                return false;
            }
            if (ss.size() > 1 && ss[0] == '0') {
                return false;
            }
            lss = ss.size();
            for (k = 0; k < lss; ++k) {
                if (!(ss[k] >= '0' && ss[k] <= '9')) {
                    return false;
                }
            }
            sscanf(ss.data(), "%d", &val);
            if (val < 0 || val > 255) {
                return false;
            }
            ++cnt;
            i = j + 1;
            ss.clear();
        }
        return cnt == 4;
    }
    
    bool validIPv6(string s) {
        int ls = s.size();
        int lss;
        int i, j, k;
        string ss;
        int val;
        int cnt;
        
        i = 0;
        cnt = 0;
        while (i < ls) {
            j = i;
            while (j < ls && s[j] != ':') {
                if (isupper(s[j])) {
                    s[j] = tolower(s[j]);
                }
                ss.push_back(s[j++]);
            }
            if (ss.size() == 0) {
                return false;
            }
            if (ss.size() > 4) {
                return false;
            }
            lss = ss.size();
            for (k = 0; k < lss; ++k) {
                if (!(ss[k] >= '0' && ss[k] <= '9') && 
                    !(ss[k] >= 'a' && ss[k] <= 'f')) {
                    return false;
                }
            }
            ++cnt;
            i = j + 1;
            ss.clear();
        }
        return cnt == 8;
    }
};
