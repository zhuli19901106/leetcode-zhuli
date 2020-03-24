// Just greedy, no game theory involved.
// Although the problem itself is not exactly easy, could be a bit tricky.
class Solution {
public:
    string predictPartyVictory(string senate) {
        auto &s = senate;
        int ls = s.size();
        
        int nr, nd;
        nr = nd = 0;
        int i;
        for (i = 0; i < ls; ++i) {
            if (senate[i] == 'R') {
                ++nr;
            } else {
                ++nd;
            }
        }
        if (nd == 0) {
            return "Radiant";
        } else if (nr == 0) {
            return "Dire";
        }
        
        int ir = nextPos(s, 'R', 0);
        int id = nextPos(s, 'D', 0);
        int cr = nr;
        int cd = nd;
        for (i = 0; i < ls; ++i) {
            if (nr == 0 || nd == 0) {
                break;
            }
            if (s[i] == 'R') {
                // choose the next 'D' to ban
                if (id < i && cd > 0) {
                    id = nextPos(s, 'D', i + 1);
                }
                s[id] = 'X';
                --nd;
                --cd;
                id = nextPos(s, 'D', id + 1);
                
                --cr;
            } else if (s[i] == 'D') {
                // choose the next 'R' to ban
                if (ir < i && cr > 0) {
                    ir = nextPos(s, 'R', i + 1);
                }
                s[ir] = 'X';
                --nr;
                --cr;
                ir = nextPos(s, 'R', ir + 1);
                
                --cd;
            } else {
                // already banned
            }
        }
        if (nd == 0) {
            return "Radiant";
        } else if (nr == 0) {
            return "Dire";
        }
        
        string s1;
        for (i = 0; i < ls; ++i) {
            if (s[i] == 'R' || s[i] == 'D') {
                s1.push_back(s[i]);
            }
        }
        return predictPartyVictory(s1);
    }
private:
    int nextPos(const string &s, char c, int idx) {
        int ls = s.size();
        int i = idx;
        while (i < ls && s[i] != c) {
            ++i;
        }
        if (i < ls && s[i] == c) {
            return i;
        }
        
        i = 0;
        while (i < idx && s[i] != c) {
            ++i;
        }
        return i;
    }
};
