// Bruteforce DFS
// I tried my old calculator, but it timed out on the case ("999999999", 80).
// I haven't found any effective pruning strategy yet.
// This solution is from https://discuss.leetcode.com/topic/76833/clean-c-dfs-solution-beating-96
#include <cstdint>
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> res;
        if (num.size() == 0) {
            return res;
        }
        string exp = "";
        dfs(num, exp, 0, 0, 0, target, res);
        
        return res;
    }
private:
    void dfs(const string &digits, string &exp, int idx, int64_t prev, 
        int64_t sum, const int64_t target, vector<string> &res) {
        int ld = digits.size();
        if (idx >= ld) {
            if (sum == target) {
                res.push_back(exp);
            }
            return;
        }
        
        int n = digits[idx] != '0' ? ld - idx : 1;
        int64_t cur = 0;
        int le = exp.size();
        string num = "";
        
        int i;
        for (i = 0; i < n; ++i) {
            num.push_back(digits[idx + i]);
            cur = cur * 10 + (digits[idx + i] - '0');
            
            if (idx == 0) {
                exp += num;
                dfs(digits, exp, idx + i + 1, cur, sum + cur, target, res);
                exp.resize(le);
            } else {
                // Insert an operator before the next number
                
                // +
                exp.push_back('+');
                exp += num;
                dfs(digits, exp, idx + i + 1, cur, sum + cur, target, res);
                exp.resize(le);
                
                // -
                exp.push_back('-');
                exp += num;
                dfs(digits, exp, idx + i + 1, -cur, sum - cur, target, res);
                exp.resize(le);
                
                // *
                exp.push_back('*');
                exp += num;
                dfs(digits, exp, idx + i + 1, prev * cur, sum + prev * (cur - 1), target, res);
                exp.resize(le);
            }
        }
    }
};
