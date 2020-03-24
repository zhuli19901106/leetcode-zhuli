// It's just a headache to meet such problems in an interview.
#include <algorithm>
#include <cctype>
#include <queue>
#include <string>
#include <vector>
using std::isdigit;
using std::islower;
using std::isupper;
using std::max;
using std::min;
using std::priority_queue;
using std::string;
using std::vector;

struct Comp {
    bool operator () (const int &x, const int &y) const {
        return x % 3 > y % 3;
    }
};

class Solution {
public:
    int strongPasswordChecker(string s) {
        int ls = s.size();
        int add = max(0, 6 - ls);
        int del = max(0, ls - 20);
        
        int type = 0;
        bool has_digit = false, has_low = false, has_up = false;
        
        int i;
        for (i = 0; i < ls; ++i) {
            if (!has_digit && isdigit(s[i])) {
                has_digit = true;
                ++type;
            } else if (!has_low && islower(s[i])) {
                has_low = true;
                ++type;
            } else if (!has_up && isupper(s[i])) {
                has_up = true;
                ++type;
            }
        }
        type = 3 - type;
        
        priority_queue<int, vector<int>, Comp> pq;
        int j;
        i = 0;
        while (i < ls) {
            j = i + 1;
            while (j < ls && s[i] == s[j]) {
                ++j;
            }
            if (j - i > 2) {
                pq.push(j - i);
            }
            i = j;
        }
        
        int res = 0;
        // Remove a char
        while (!pq.empty() && del > 0) {
            i = pq.top();
            pq.pop();
            if (i - 1 >= 3) {
                pq.push(i - 1);
            }
            
            ++res;
            --del;
        }
        
        // Add a char
        while (!pq.empty() && add > 0) {
            i = pq.top();
            pq.pop();
            if (i - 2 >= 3) {
                pq.push(i - 2);
            }
            
            ++res;
            --add;
            --type;
        }
        type = max(0, type);
        
        // Change a char
        while (!pq.empty()) {
            i = pq.top();
            pq.pop();
            
            res += i / 3;
            type = (type > i / 3 ? type - i / 3 : 0);
        }
        add = max(0, add - type);
        res += type;
        res += add;
        res += del;
        
        return res;
    }
};
