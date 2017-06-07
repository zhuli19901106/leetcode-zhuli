// Lame, dude.
#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using std::min;
using std::string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        unordered_map<string, int> um;
        int n1 = list1.size();
        int n2 = list2.size();
        
        for (string &s: list1) {
            ++um[s];
        }
        for (string &s: list2) {
            ++um[s];
        }
        
        auto it = um.begin();
        while (it != um.end()) {
            if (it->second == 1) {
                it = um.erase(it);
            } else {
                it->second = 0;
                ++it;
            }
        }
        
        int i;
        for (i = 0; i < n1; ++i) {
            if (um.find(list1[i]) != um.end()) {
                um[list1[i]] += i;
            }
        }
        for (i = 0; i < n2; ++i) {
            if (um.find(list2[i]) != um.end()) {
                um[list2[i]] += i;
            }
        }
        
        int min_sum = n1 + n2;
        for (auto &p: um) {
            min_sum = min(min_sum, p.second);
        }
        
        vector<string> res;
        for (auto &p: um) {
            if (p.second == min_sum) {
                res.push_back(p.first);
            }
        }
        um.clear();
        
        return res;
    }
};
