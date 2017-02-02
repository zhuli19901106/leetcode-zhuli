// DFS with backtracking
// If the datasets were larger, memorization would be needed.
#include <algorithm>
#include <climits>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
using std::make_pair;
using std::min;
using std::pair;
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    int findMinStep(string board, string hand) {
        vector<pair<char, int>> v;
        unordered_map<char, int> um;
        
        int ls = board.size();
        int i, j;
        
        i = 0;
        while (i < ls) {
            j = i + 1;
            while (j < ls && board[i] == board[j]) {
                ++j;
            }
            v.push_back(make_pair(board[i], j - i));
            i = j;
        }
        
        ls = hand.size();
        for (i = 0; i < ls; ++i) {
            ++um[hand[i]];
        }
        
        int res = dfs(v, um);
        
        v.clear();
        um.clear();
        
        return res != INT_MAX ? res : -1;
    }
private:
    static const int NUM_ELIMINATE = 3;
    
    int dfs(vector<pair<char, int>> &v, unordered_map<char, int> &um) {
        if (v.size() == 0) {
            return 0;
        }
        
        int res = INT_MAX;
        int i, j;
        int need;
        int sum;
        int n = v.size();
        vector<pair<char, int>> v1;
        
        for (i = 0; i < n; ++i) {
            need = NUM_ELIMINATE - v[i].second;
            if (um[v[i].first] < need) {
                continue;
            }
            
            um[v[i].first] -= need;
            v1 = v;
            
            v.erase(v.begin() + i);
            j = i - 1;
            while (j >= 0 && j + 1 < v.size() && v[j].first == v[j + 1].first) {
                v[j].second += v[j + 1].second;
                v.erase(v.begin() + j + 1);
                
                if (v[j].second >= NUM_ELIMINATE) {
                    v.erase(v.begin() + j);
                    --j;
                } else {
                    break;
                }
            }
            
            sum = dfs(v, um);
            
            v = v1;
            um[v[i].first] += need;
            
            if (sum < INT_MAX) {
                res = min(res, sum + need);
            }
        }
        
        return res;
    }
};
