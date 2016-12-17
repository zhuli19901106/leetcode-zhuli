#include <algorithm>
using std::max;
using std::min;

class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int x1, y1, x2, y2;
        x1 = max(A, E);
        y1 = max(B, F);
        x2 = min(C, G);
        y2 = min(D, H);
        x2 = max(x1, x2);
        y2 = max(y1, y2);
        return (C - A) * (D - B) + (G - E) * (H - F) - (x2 - x1) * (y2 - y1);
    }
};
