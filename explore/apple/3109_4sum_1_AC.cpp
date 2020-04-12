#include <algorithm>
#include <string>
#include <unordered_set>
using std::sort;
using std::string;
using std::unordered_set;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        unordered_set<string> hash;
        vector<vector<int>> res;
        vector<int> tuple(4);
        int i1, i2, i3, i4;
        int n = nums.size();
        int sum;
        string s;
        
        sort(nums.begin(), nums.end());
        for (i1 = 0; i1 < n; ++i1) {
            tuple[0] = nums[i1];
            for (i2 = i1 + 1; i2 < n; ++i2) {
                tuple[1] = nums[i2];
                i3 = i2 + 1;
                i4 = n - 1;
                while (i3 < i4) {
                    sum = nums[i1] + nums[i2] + nums[i3] + nums[i4];
                    if (sum < target) {
                        ++i3;
                    } else if (sum > target) {
                        --i4;
                    } else {
                        tuple[2] = nums[i3];
                        tuple[3] = nums[i4];
                        s = sign(tuple);
                        if (hash.find(s) == hash.end()) {
                            res.push_back(tuple);
                            hash.insert(s);
                        }
                        do {
                            ++i3;
                        } while (i3 < i4 && nums[i3 - 1] == nums[i3]);
                    }
                }
            }
        }
        hash.clear();
        return res;
    }
private:
    string sign(vector<int> &v) {
        int n = v.size();
        if (n == 0) {
            return "";
        }
        int i;
        string s = to_string(v[0]);
        for (i = 1; i < n; ++i) {
            s.push_back(' ');
            s += to_string(v[i]);
        }
        return s;
    }
};
