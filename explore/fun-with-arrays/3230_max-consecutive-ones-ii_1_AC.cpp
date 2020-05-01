// Not so hard, but a bit tricky.
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        auto &a = nums;
        int n = a.size();
        if (n <= 1) {
            return n;
        }
        
        int last1 = 0;
        int last0 = 0;
        int cur = 0;
        int type = 0;
        
        int res = 1;
        int i;
        for (i = 0; i < n; ++i) {
            if (a[i] == 1) {
                if (type == 0) {
                    last0 = cur;
                    cur = 1;
                    type = 1;
                } else {
                    ++cur;
                }
                
                if (last0 == 1) {
                    res = max(res, cur + 1 + last1);
                } else if (last0 > 1) {
                    res = max(res, cur + 1);
                } else {
                    res = max(res, cur);
                }
            } else {
                if (type == 0) {
                    ++cur;
                } else {
                    last1 = cur;
                    cur = 1;
                    type = 0;
                    
                    res = max(res, last1 + 1);
                }
            }
        }
        
        return res;
    }
};
