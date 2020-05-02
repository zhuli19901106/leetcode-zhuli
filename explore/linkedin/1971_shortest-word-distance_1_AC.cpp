#include <algorithm>
#include <string>
#include <vector>
using std::min;
using std::string;
using std::vector;

class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int n = words.size();
        int res = n;
        int last = 0, cur = 0;
        int last_i = 0;
        int i;
        for (i = 0; i < n; ++i) {
            if (words[i] == word1) {
                cur = -1;
            } else if (words[i] == word2) {
                cur = +1;
            } else {
                cur = 0;
            }
            
            if (cur != 0) {
                if (cur + last == 0) {
                    res = min(res, i - last_i);
                }
                last = cur;
                last_i = i;
            }
        }
        return res;
    }
};
