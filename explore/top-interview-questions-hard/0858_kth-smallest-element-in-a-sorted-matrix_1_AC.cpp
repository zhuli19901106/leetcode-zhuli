// Young Tableau, an interesting data structure
// O(k * log(k)) solution with heap
#include <algorithm>
#include <queue>
#include <vector>
using std::priority_queue;
using std::vector;

typedef struct Elem {
    int x;
    int y;
    int val;
    
    Elem() {}
    
    Elem(int _x, int _y, int _val): x(_x), y(_y), val(_val) {}
} Elem;

struct Comparator {
    bool operator () (const Elem &e1, const Elem &e2) {
        return e1.val > e2.val;
    }
};

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        priority_queue<Elem, vector<Elem>, Comparator> pq;
        vector<vector<bool>> mark(n, vector<bool>(n, false));
        Elem e1;
        int i;
        int res;
        
        pq.push(Elem(0, 0, matrix[0][0]));
        mark[0][0] = true;
        for (i = 0; i < k; ++i) {
            // Make sure nothing is pushed twice
            e1 = pq.top();
            pq.pop();
            mark[e1.x][e1.y] = true;
            res = e1.val;
            
            if (e1.x + 1 < n && !mark[e1.x + 1][e1.y]) {
                pq.push(Elem(e1.x + 1, e1.y, matrix[e1.x + 1][e1.y]));
                mark[e1.x + 1][e1.y] = true;
            }
            if (e1.y + 1 < n && !mark[e1.x][e1.y + 1]) {
                pq.push(Elem(e1.x, e1.y + 1, matrix[e1.x][e1.y + 1]));
                mark[e1.x][e1.y + 1] = true;
            }
        }
        
        mark.clear();
        while (!pq.empty()) {
            pq.pop();
        }
        
        return res;
    }
};
