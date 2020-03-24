// Plain and simple
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<bool> cnt(n, false);
        vector<int> res;
        int i;
        
        for (i = 0; i < n; ++i) {
            cnt[nums[i] - 1] = true;
        }
        for (i = 0; i < n; ++i) {
            if (!cnt[i]) {
                res.push_back(i + 1);
            }
        }
        cnt.clear();
        return res;
    }
};
