// IIRC, a same problem has already been posted.
/*
// Employee info
class Employee {
public:
    // It's the unique ID of each node.
    // unique id of this employee
    int id;
    // the importance value of this employee
    int importance;
    // the id of direct subordinates
    vector<int> subordinates;
};
*/
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    int getImportance(vector<Employee*> employees, int id) {
        unordered_map<int, int> dj;
        unordered_map<int, int> imp;
        
        for (auto &e: employees) {
            if (dj.find(e->id) == dj.end()) {
                dj[e->id] = e->id;
            }
            for (auto &sid: e->subordinates) {
                if (sid == id) {
                    continue;
                }
                dj[sid] = e->id;
            }
        }
        
        int sum = 0;
        for (auto &e: employees) {
            if (findRoot(dj, e->id) == id) {
                sum += e->importance;
            }
        }
        
        return sum;
    }
private:
    int findRoot(unordered_map<int, int> &dj, int x) {
        if (dj.find(x) == dj.end()) {
            return x;
        }
        int r = x;
        while (r != dj[r]) {
            r = dj[r];
        }
        int k = x;
        while (x != r) {
            x = dj[x];
            dj[k] = r;
            k = x;
        }
        return r;
    }
};
