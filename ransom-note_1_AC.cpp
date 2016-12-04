#include <cstring>
using std::memset;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        const int DICT_SIZE = 26;
        int cnt[DICT_SIZE];
        memset(cnt, 0, DICT_SIZE * sizeof(int));
        
        int nr = ransomNote.size();
        int i;
        for (i = 0; i < nr; ++i) {
            --cnt[ransomNote[i] - 'a'];
        }
        int nm = magazine.size();
        for (i = 0; i < nm; ++i) {
            ++cnt[magazine[i] - 'a'];
        }
        for (i = 0; i < DICT_SIZE; ++i) {
            if (cnt[i] < 0) {
                return false;
            }
        }
        return true;
    }
};
