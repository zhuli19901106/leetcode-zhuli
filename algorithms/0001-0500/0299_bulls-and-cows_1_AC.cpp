#include <algorithm>
#include <cstring>
#include <string>
using std::memset;
using std::min;
using std::to_string;

class Solution {
public:
    string getHint(string secret, string guess) {
        const int DICT_SIZE = 10;
        int cnt1[DICT_SIZE], cnt2[DICT_SIZE];
        int bull = 0;
        int cow = 0;
        int n = secret.size();
        int i;
        memset(cnt1, 0, DICT_SIZE * sizeof(int));
        memset(cnt2, 0, DICT_SIZE * sizeof(int));
        for (i = 0; i < n; ++i) {
            ++cnt1[secret[i] - '0'];
            ++cnt2[guess[i] - '0'];
            if (secret[i] == guess[i]) {
                ++bull;
            }
        }
        for (i = 0; i < DICT_SIZE; ++i) {
            cow += min(cnt1[i], cnt2[i]);
        }
        cow -= bull;
        return to_string(bull) + "A" + to_string(cow) + "B";
    }
};
