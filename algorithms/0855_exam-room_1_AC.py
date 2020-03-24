// https://leetcode.com/problems/exam-room/
// 1AC, I need a tree set, yet python doesn't have one for builtin
#include <algorithm>
#include <set>
using std::next;
using std::set;

class ExamRoom {
public:
    ExamRoom(int N) {
        this->n = N;
    }

    int seat() {
        auto &st = this->st;

        int ans = -1;
        int max_dist = 0;
        if (st.empty()) {
            ans = 0;
            st.insert(ans);
            return ans;
        }

        int i1, i2;
        if (st.find(0) == st.end()) {
            i1 = *st.begin();
            if (i1 > max_dist) {
                max_dist = i1;
                ans = 0;
            }
        }

        auto it = st.begin();
        auto it1 = it;
        int dist;
        int mid;
        while (it != st.end()) {
            it1 = next(it);
            if (it1 == st.end()) {
                break;
            }
            i1 = *it;
            i2 = *it1;
            mid = i1 + (i2 - i1) / 2;
            dist = mid - i1;
            if (dist > max_dist) {
                max_dist = dist;
                ans = mid;
            }
            ++it;
        }

        if (st.find(n - 1) == st.end()) {
            i1 = *st.rbegin();
            if (n - 1 - i1 > max_dist) {
                max_dist = i1;
                ans = n - 1;
            }
        }
        st.insert(ans);

        return ans;
    }
    
    void leave(int p) {
        this->st.erase(p);
    }
private:
    set<int> st;
    int n;
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom* obj = new ExamRoom(N);
 * int param_1 = obj->seat();
 * obj->leave(p);
 */