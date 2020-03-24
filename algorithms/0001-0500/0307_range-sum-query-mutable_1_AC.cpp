// Binary indexed tree
class NumArray {
public:
    NumArray(vector<int> nums) {
        this->n = nums.size();
        this->v.resize(n + 1, 0);
        int i;
        for (i = 0; i < n; ++i) {
            add(i + 1, nums[i]);
        }
    }
    
    void update(int i, int val) {
        add(i + 1, val - get(i + 1));
    }
    
    int sumRange(int i, int j) {
        return sum(j + 1) - sum(i);
    }
    
private:
    vector<int> v;
    int n;
    
    int lowbit(int x) {
        return x & -x;
    }
    
    void add(int i, int val) {
        int idx = i;
        while (idx <= n) {
            v[idx] += val;
            idx += lowbit(idx);
        }
    }
    
    int get(int i) {
        return sum(i) - sum(i - 1);
    }
    
    int sum(int i) {
        int idx = i;
        int res = 0;
        while (idx > 0) {
            res += v[idx];
            idx -= lowbit(idx);
        }
        return res;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
