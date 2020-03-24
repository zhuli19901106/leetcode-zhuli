#include <unordered_set>
using std::unordered_set;

// Forward declaration of the knows API.
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        unordered_set<int> us;
        int i;
        for (i = 0; i < n; ++i) {
            us.insert(i);
        }
        
        bool suc;
        int j;
        i = 0;
        while (us.size() > 0) {
            if (suc) {
                i = *(us.begin());
            }
            suc = true;
            for (auto it = us.begin(); it != us.end(); ++it) {
                j = *it;
                if (i == j) {
                    continue;
                }
                if (knows(i, j)) {
                    us.erase(i);
                    i = j;
                    suc = false;
                    break;
                }
            }
            if (suc) {
                if (isCelebrity(i, n)) {
                    return i;
                } else {
                    us.erase(i);
                }
            }
        }
        return -1;
    }
private:
    int isCelebrity(int x, int n) {
        int i;
        for (i = 0; i < n; ++i) {
            if (x == i) {
                continue;
            }
            if (knows(x, i) || !knows(i, x)) {
                return false;
            }
        }
        return true;
    }
};
