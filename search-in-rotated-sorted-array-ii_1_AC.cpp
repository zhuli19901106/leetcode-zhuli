class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int n = nums.size();
        int ll = 0;
        int rr = n - 1;
        int mm;
        
        while (ll <= rr) {
            mm = ll + (rr - ll >> 1);
            if (nums[ll] < target && target < nums[mm]) {
                rr = mm - 1;
            } else if (nums[mm] < target && target < nums[rr]) {
                ll = mm + 1;
            } else {
                if (nums[ll] == target) {
                    return true;
                } else {
                    ++ll;
                }
                if (nums[rr] == target) {
                    return true;
                } else {
                    --rr;
                }
            }
        }
        return false;
    }
};
