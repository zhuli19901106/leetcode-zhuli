// I think the problem is poorly specified.
// If it's supposed to be an OO or system design problem, much more have to be said.
#include <cstdint>
#include <cstdio>
#include <map>
#include <string>
#include <vector>
using std::map;
using std::sscanf;
using std::string;
using std::vector;

class LogSystem {
public:
    LogSystem() {
        string legend = "Year:Month:Day:Hour:Minute:Second";
        vl = split(legend, ':');
        
        int n = vl.size();
        int i;
        for (i = 0; i < n; ++i) {
            gi[vl[i]] = i;
        }
        
        int64_t conv[] = {366, 31, 24, 60, 60, 1};
        n = sizeof(conv) / sizeof(int64_t);
        for (i = 0; i < n; ++i) {
            vc.push_back(conv[i]);
        }
        
        n = vc.size();
        vc_pro.resize(n);
        vc_pro[n - 1] = vc[n - 1];
        for (i = n - 2; i >= 0; --i) {
            vc_pro[i] = vc_pro[i + 1] * vc[i];
        }
    }
    
    void put(int id, string timestamp) {
        int64_t ts = getTimestamp(timestamp);
        logs[ts] = id;
    }
    
    vector<int> retrieve(string s, string e, string gra) {
        int gra_idx = gi[gra];
        int64_t g = vc_pro[gra_idx];
        int64_t ts = getTimestamp(s) / g * g;
        int64_t te = (getTimestamp(e) / g + 1) * g;
        
        map<int64_t, int>::iterator it1, it2;
        it1 = logs.lower_bound(ts);
        it2 = logs.lower_bound(te);
        vector<int> res;
        for (auto it = it1; it != it2; ++it) {
            res.push_back(it->second);
        }
        
        return res;
    }
private:
    vector<string> vl;
    vector<int64_t> vc;
    vector<int64_t> vc_pro;
    unordered_map<string, int> gi;
    map<int64_t, int> logs;
     
    vector<string> split(const string &s, char del) {
        vector<string> vs;
        string ss;
        int ls = s.size();
        int i;
        for (i = 0; i < ls; ++i) {
            if (s[i] != del) {
                ss.push_back(s[i]);
            } else {
                if (ss.size() > 0) {
                    vs.push_back(ss);
                    ss.clear();
                }
            }
        }
        if (ss.size() > 0) {
            vs.push_back(ss);
            ss.clear();
        }
        
        return vs;
    }
    
    int64_t getTimestamp(const string &s) {
        vector<string> vs = split(s, ':');
        int64_t res = 0;
        int n = vs.size();
        int i;
        int64_t val;
        for (i = 0; i < n; ++i) {
            sscanf(vs[i].data(), "%lld", &val);
            res += val * vc_pro[i];
        }
        
        return res;
    }
};

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem obj = new LogSystem();
 * obj.put(id,timestamp);
 * vector<int> param_2 = obj.retrieve(s,e,gra);
 */
