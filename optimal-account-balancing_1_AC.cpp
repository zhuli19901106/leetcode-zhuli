// 1AC, the key is to find the maximal number of partitions, where each of them sums up to 0.
#include <iterator>
#include <unordered_map>
#include <vector>
using std::next;
using std::unordered_map;
using std::vector;

typedef unordered_map<int, int> UMII;
typedef UMII::iterator UMII_IT;

class Solution {
public:
    int minTransfers(vector<vector<int>>& transactions) {
        UMII acc;
        int i, j, val;
        for (auto &v: transactions) {
            i = v[0];
            j = v[1];
            val = v[2];
            acc[i] -= val;
            acc[j] += val;
        }
        
        UMII pos, neg;
        int n = 0;
        for (auto &p: acc) {
            if (p.second == 0) {
                continue;
            }
            if (p.second > 0) {
                ++pos[p.second];
            } else {
                ++neg[p.second];
            }
            ++n;
        }
        acc.clear();
        
        UMII pos1, neg1;
        int k = 0;
        while (pos.size() > 0) {
            // Search for subsets that sum up to zero
            (void)dfsNeg(neg.begin(), 0, pos1, neg1, pos, neg);
            remove(pos, pos1);
            remove(neg, neg1);
            ++k;
        }
        pos.clear();
        neg.clear();
        pos1.clear();
        neg1.clear();
        
        return n - k;
    }
private:
    void remove(UMII &um, UMII &um1) {
        for (auto it = um1.begin(); it != um1.end(); ++it) {
            if (um[it->first] <= it->second) {
                um.erase(it->first);
            } else {
                um[it->first] -= it->second;
            }
        }
    }
    
    bool dfsNeg(UMII_IT it, int sum, UMII &pos1, UMII &neg1, UMII &pos, 
        UMII &neg) {
        if (it == neg.end()) {
            if (sum == 0) {
                return false;
            }
            return dfsPos(pos.begin(), 0, -sum, pos1, pos);
        }
        
        int c = it->second;
        int i;
        for (i = 0; i <= c; ++i) {
            neg1[it->first] = i;
            if (dfsNeg(next(it), sum + i * it->first, pos1, neg1, pos, neg)) {
                return true;
            }
        }
        // You're not supposed to be here.
        return false;
    }
    
    bool dfsPos(UMII_IT it, int sum, int target, UMII &pos1, UMII &pos) {
        if (it == pos.end()) {
            return sum == target;
        }
        
        int c = it->second;
        int i;
        for (i = 0; i <= c && sum + i * it->first <= target; ++i) {
            pos1[it->first] = i;
            if (dfsPos(next(it), sum + i * it->first, target, pos1, pos)) {
                return true;
            }
        }
        return false;
    }
};
