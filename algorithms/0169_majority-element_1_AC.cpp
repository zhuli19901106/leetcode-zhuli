class Solution {
public:
    int majorityElement(vector<int> &nums) {
        vector<int> &a = nums;
        int n = a.size();
        
        int i, res = a[0], cnt = 1;
        for (i = 1; i < n; ++i) {
            res == a[i] ? ++cnt : (cnt == 1 ? res = a[i] : --cnt);
        }
        
        // Majority element is guaranteed to exist, so skip the checking.
        return res;
    }
};
