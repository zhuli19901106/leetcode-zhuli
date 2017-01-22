#include <string>
using std::string;
using std::to_string;

class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> res;
        int n = nums.size();
        if (n < 2) {
            return res;
        }
        vector<int> seq;
        unordered_set<string> hash;
        
        dfs(0, nums, seq, res, hash);
        hash.clear();
        return res;
    }
private:
    void dfs(int idx, vector<int> &nums, vector<int> &seq, 
        vector<vector<int>> &res, unordered_set<string> &hash) {
        if (idx >= nums.size()) {
            string s = sign(seq);
            if (seq.size() >= 2 && hash.find(s) == hash.end()) {
                res.push_back(seq);
                hash.insert(s);
            }
            return;
        }
        
        dfs(idx + 1, nums, seq, res, hash);
        if (!seq.empty() && seq.back() > nums[idx]) {
            return;
        }
        seq.push_back(nums[idx]);
        dfs(idx + 1, nums, seq, res, hash);
        seq.pop_back();
    }
    
    string sign(vector<int> &v) {
        string s = "";
        int n = v.size();
        int i;
        for (i = 0; i < n; ++i) {
            s += to_string(v[i]) + " ";
        }
        return s;
    }
};
