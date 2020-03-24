#include <algorithm>
#include <string>
#include <vector>
using std::min;
using std::string;
using std::vector;

class Solution {
public:
    int shortestWordDistance(vector<string>& words, string word1, string word2) {
        int n = words.size();
        int res = n;
        int i, last_i;
        int tag, last_tag;
        
        last_i = -1;
        last_tag = 0;
        for (i = 0; i < n; ++i) {
            if (last_tag == -1) {
                if (words[i] == word2) {
                    tag = +1;
                } else if (words[i] == word1) {
                    tag = -1;
                } else {
                    continue;
                }
            } else {
                if (words[i] == word1) {
                    tag = -1;
                } else if (words[i] == word2) {
                    tag = +1;
                } else {
                    continue;
                }
            }
            if (last_tag + tag == 0) {
                res = min(res, i - last_i);
            }
            last_i = i;
            last_tag = tag;
        }
        
        return res;
    }
};
