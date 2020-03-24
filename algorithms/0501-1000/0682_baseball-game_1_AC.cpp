#include <cstdio>
#include <string>
#include <vector>
using std::sscanf;
using std::string;
using std::vector;

class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> v;
        int num;
        for (auto &op: ops) {
            if (op == "C") {
                v.pop_back();
            } else if (op == "D") {
                v.push_back(v.back() * 2);
            } else if (op == "+") {
                num = v.size();
                v.push_back(v[num - 1] + v[num - 2]);
            } else {
                sscanf(op.data(), "%d", &num);
                v.push_back(num);
            }
        }
        
        int sum = 0;
        for (auto &x: v) {
            sum += x;
        }
        
        return sum;
    }
};
