class NumArray {
public:
    NumArray(vector<int> &nums) {
        n = nums.size();
        a.resize(n + 1);
        int i;
        int s = 0;
        for (i = 0; i < n; ++i) {
            a[i + 1] = a[i] + nums[i];
        }
    }

    int sumRange(int i, int j) {
        return a[j + 1] - a[i];
    }
    
    ~NumArray() {
        a.clear();
    }
private:
    vector<int> a;
    int n;
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
