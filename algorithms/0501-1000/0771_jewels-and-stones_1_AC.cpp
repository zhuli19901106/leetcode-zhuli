// easy
// https://leetcode.com/problems/jewels-and-stones/
#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        unordered_set<char> us;
        for (auto &ch: J) {
            us.insert(ch);
        }
        int count = 0;
        for (auto &ch: S) {
            if (us.find(ch) != us.end()) {
                ++count;
            }
        }
        return count;
    }
};
