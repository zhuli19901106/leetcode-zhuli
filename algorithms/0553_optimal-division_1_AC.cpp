#include <string>
#include <vector>
using std::string;
using std::to_string;
using std::vector;

class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        int n = nums.size();
        vector<vector<double>> vp_min(n, vector<double>(n));
        vector<vector<double>> vp_max(n, vector<double>(n));
        vector<vector<string>> vs_min(n, vector<string>(n));
        vector<vector<string>> vs_max(n, vector<string>(n));
        
        int i;
        for (i = 0; i < n; ++i) {
            vp_min[i][i] = vp_max[i][i] = nums[i];
            vs_min[i][i] = vs_max[i][i] = to_string(nums[i]);
        }
        
        int j, k;
        double p;
        for (i = 1; i < n; ++i) {
            for (j = 0; j + i < n; ++j) {
                vp_min[j][j + i] = vp_min[j][j + i - 1] / vp_max[j + i][j + i];
                vs_min[j][j + i] = vs_min[j][j + i - 1] + "/" + vs_max[j + i][j + i];
                
                vp_max[j][j + i] = vp_max[j][j + i - 1] / vp_min[j + i][j + i];
                vs_max[j][j + i] = vs_max[j][j + i - 1] + "/" + vs_min[j + i][j + i];
                
                for (k = j + 1; k < j + i; ++k) {
                    p = vp_max[j][k - 1] / vp_min[k][j + i];
                    if (p > vp_max[j][j + i]) {
                        vp_max[j][j + i] = p;
                        vs_max[j][j + i] = vs_max[j][k - 1] + "/(" + vs_min[k][j + i] + ")";
                    }
                    
                    p = vp_min[j][k - 1] / vp_max[k][j + i];
                    if (p < vp_min[j][j + i]) {
                        vp_min[j][j + i] = p;
                        vs_min[j][j + i] = vs_min[j][k - 1] + "/(" + vs_max[k][j + i] + ")";
                    }
                }
            }
        }
        
        string res = vs_max[0][n - 1];
        vp_min.clear();
        vp_max.clear();
        vs_min.clear();
        vs_max.clear();
        
        return res;
    }
};
