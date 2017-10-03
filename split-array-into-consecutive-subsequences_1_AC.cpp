#include <map>
using std::map;

class Solution {
public:
    bool isPossible(vector<int>& nums) {
        map<int, int> mm;
        for (auto &num: nums) {
            ++mm[num];
        }
        while (!mm.empty()) {
            if (removeSeq(mm) < 3) {
                return false;
            }
        }
        return true;
    }
private:
    int removeSeq(map<int, int> &mm) {
        map<int, int>::iterator it;
        int res = 0;
        int cc = 0;
        int old_val;
        
        it = mm.begin();
        while (it != mm.end()) {
            if (it->second < cc) {
                break;
            }
            ++res;
            cc = it->second;
            
            old_val = it->first;
            if (it->second == 1) {
                it = mm.erase(it);
            } else {
                --(it->second);
                ++it;
            }
            if (it != mm.end() && it->first != old_val + 1) {
                break;
            }
        }
        
        return res;
    }
};
