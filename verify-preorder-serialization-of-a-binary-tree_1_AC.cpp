class Solution {
public:
    bool isValidSerialization(string preorder) {
        vector<bool> v;
        parse(preorder, v);
        int idx = 0;
        bool res = (traverse(v, idx) && idx == v.size());
        v.clear();
        return res;
    }
private:
    void parse(string &s, vector<bool> &v) {
        int ls = s.size();
        int i = 0;
        while (i < ls) {
            v.push_back(s[i] != '#');
            while (i < ls && s[i] != ',') {
                ++i;
            }
            ++i;
        }
    }
    
    bool traverse(vector<bool> &v, int &idx) {
        if (idx == v.size()) {
            return false;
        }
        if (!v[idx++]) {
            return true;
        } else {
            if (!traverse(v, idx)) {
                return false;
            }
            if (!traverse(v, idx)) {
                return false;
            }
            return true;
        }
    }
};
