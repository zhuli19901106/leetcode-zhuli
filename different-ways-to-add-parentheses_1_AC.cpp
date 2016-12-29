#include <algorithm>
#include <cctype>
#include <sstream>
using std::isdigit;
using std::sort;
using std::stringstream;
using std::unordered_set;

class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> res;
        splitToken(input);
        compute(0, nums.size() - 1, res);
        nums.clear();
        ops.clear();
        sort(res.begin(), res.end());
        
        return res;
    }
private:
    vector<int> nums;
    vector<string> ops;
    
    void splitToken(string &s) {
        stringstream ss;
        ss << s;
        int num;
        char ch[2] = "?";
        
        ss >> num;
        nums.push_back(num);
        while (true) {
            if (ss >> ch[0]) {
                ops.push_back(string(ch));
            } else {
                break;
            }
            if (ss >> num) {
                nums.push_back(num);
            } else {
                break;
            }
        }
    }
    
    int calc(int x, int y, const string &op) {
        if (op == "+") {
            return x + y;
        }
        if (op == "-") {
            return x - y;
        }
        if (op == "*") {
            return x * y;
        }
        return 0;
    }
    
    void compute(int left, int right, vector<int> &res) {
        if (left == right) {
            res.push_back(nums[left]);
            return;
        }
        
        int i, j, k;
        int n1, n2;
        vector<int> res1, res2;
        for (i = left; i < right; ++i) {
            compute(left, i, res1);
            compute(i + 1, right, res2);
            n1 = res1.size();
            n2 = res2.size();
            for (j = 0; j < n1; ++j) {
                for (k = 0; k < n2; ++k) {
                    res.push_back(calc(res1[j], res2[k], ops[i]));
                }
            }
            res1.clear();
            res2.clear();
        }
    }
};
