#include <iterator>
#include <map>
using std::prev;
using std::map;

class MyCalendar {
public:
    MyCalendar() {}
    
    bool book(int start, int end) {
        bool left_ok = false;
        bool right_ok = false;
        
        if (mm.empty() || end <= mm.begin()->first || start >= mm.rbegin()->second) {
            left_ok = right_ok = true;
        }
        map<int, int>::iterator it;
        it = mm.lower_bound(start);
        if (it == mm.begin() || prev(it)->second <= start) {
            left_ok = true;
        }
        if (it == mm.end() || end <= it->first) {
            right_ok = true;
        }
        
        if (left_ok && right_ok) {
            mm[start] = end;
            return true;
        } else {
            return false;
        }
    }
    
    ~MyCalendar() {
        mm.clear();
    }
private:
    map<int, int> mm;
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.book(start,end);
 */
