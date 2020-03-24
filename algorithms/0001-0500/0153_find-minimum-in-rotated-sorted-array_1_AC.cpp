class Solution {
public:
    int findMin(vector<int>& nums) {
        int n = nums.size();
        int ll, mm, rr;
        
        ll = 0;
        rr = n - 1;
        if (nums[ll] <= nums[rr]) {
            return nums[ll];
        }
        while (rr - ll > 1) {
            mm = ll + (rr - ll >> 1);
            if (nums[mm] > nums[ll]) {
                ll = mm;
            } else {
                rr = mm; 
            }
        }
        return nums[rr];
    }
};
