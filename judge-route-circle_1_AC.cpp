#include <string>
#include <unordered_map>
using std::string;
using std::unordered_map;

class Solution {
public:
    bool judgeCircle(string moves) {
        unordered_map<char, int> um;
        for (auto &c: moves) {
            ++um[c];
        }
        return (um['L'] == um['R'] && um['U'] == um['D']);
    }
};
