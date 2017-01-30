#include <algorithm>
#include <string>
#include <vector>
using std::sort;
using std::string;
using std::to_string;
using std::vector;

bool comparator(const string &s1, const string &s2)
{
    return s1 + s2 > s2 + s1;
}

class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> v;
        int n = nums.size();
        int i;
        for (i = 0; i < n; ++i) {
            v.push_back(to_string(nums[i]));
        }
        sort(v.begin(), v.end(), comparator);
        string res = "";
        for (i = 0; i < n; ++i) {
            res += v[i];
        }
        
        n = res.size();
        i = 0;
        while (i < n - 1 && res[i] == '0') {
            ++i;
        }
        v.clear();
        return res.substr(i, n - i);
    }
};
