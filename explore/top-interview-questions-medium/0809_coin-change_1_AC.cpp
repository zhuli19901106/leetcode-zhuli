#include <unordered_map>
#include <unordered_set>
using std::unordered_map;
using std::unordered_set;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount < 0) {
            return -1;
        }
        if (amount == 0) {
            return 0;
        }
        int nc = coins.size();
        if (nc == 0) {
            return -1;
        }
        int gd = coins[0];
        int i;
        for (i = 1; i < nc; ++i) {
            if (coins[i] > amount) {
                continue;
            }
            gd = gcd(gd, coins[i]);
        }
        if (amount % gd != 0) {
            return -1;
        }
        
        vector<unordered_set<int>> us(2);
        unordered_map<int, int> um;
        int f, nf;
        int round;
        
        us[0].insert(0);
        um[0] = 0;
        f = 1;
        nf = !f;
        round = 0;
        while (true) {
            ++round;
            for (i = 0; i < nc; ++i) {
                if (coins[i] > amount) {
                    continue;
                }
                for (auto it = us[nf].begin(); it != us[nf].end(); ++it) {
                    if (*it + coins[i] > amount) {
                        continue;
                    }
                    if (um.find(*it + coins[i]) != um.end()) {
                        continue;
                    }
                    us[f].insert(*it + coins[i]);
                    um[*it + coins[i]] = round;
                }
            }
            us[nf].clear();
            if (um.find(amount) != um.end()) {
                break;
            } else if (us[f].size() == 0) {
                round = -1;
                break;
            } else {
                f = !f;
                nf = !f;
            }
        }
        us.clear();
        um.clear();
        return round;
    }
private:
    int gcd(int x, int y) {
        int t;
        while (x % y != 0) {
            t = x;
            x = y;
            y = t % x;
        }
        return y;
    }
};
