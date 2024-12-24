// medium
// https://leetcode.com/problems/design-a-leaderboard/
// I need a tree map
#include <map>
#include <unordered_map>
#include <unordered_set>
using std::map;
using std::unordered_map;
using std::unordered_set;

class Leaderboard {
public:
    Leaderboard() {}

    ~Leaderboard() {
        mb.clear();
        ms.clear();
    }

    void addScore(int playerId, int score) {
        if (score == 0) {
            return;
        }

        int sc;
        if (ms.find(playerId) == ms.end()) {
            ms[playerId] = score;
            mb[score].insert(playerId);
        } else {
            sc = ms[playerId];
            ms[playerId] += score;
            mb[sc].erase(playerId);
            if (mb[sc].empty()) {
                mb.erase(sc);
            }
            mb[sc + score].insert(playerId);
        }
    }

    int top(int K) {
        int cnt = 0;
        int sum = 0;
        int sc;
        for (auto it1 = mb.rbegin(); it1 != mb.rend(); ++it1) {
            sc = it1->first;
            auto &mbs = it1->second;
            int n = mbs.size();
            for (int i = 0; i < n; ++i) {
                sum += sc;
                ++cnt;
                if (cnt == K) {
                    break;
                }
            }
            if (cnt == K) {
                break;
            }
        }
        return sum;
    }

    void reset(int playerId) {
        if (ms.find(playerId) == ms.end()) {
            return;
        }
        int sc = ms[playerId];
        // reset the score to 0, not remove it
        this->addScore(playerId, -sc);
    }
private:
    map<int, unordered_set<int>> mb;
    unordered_map<int, int> ms;
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */
