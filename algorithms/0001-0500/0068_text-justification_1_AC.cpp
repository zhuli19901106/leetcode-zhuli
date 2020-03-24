class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        auto &w = words;
        int nw = w.size();
        int L = maxWidth;
        int i, j, k;
        int len;
        string line;
        
        int c1, c2;
        int ci;
        
        i = 0;
        while (i < nw) {
            j = i;
            len = 0;
            while (j < nw) {
                len += w[j].size();
                if (len + j - i > L) {
                    len -= w[j].size();
                    break;
                }
                ++j;
            }
            
            line.clear();
            if (j - i == 1 || j == nw) {
                // Left aligned
                while (i < j) {
                    line += w[i++];
                    line.push_back(' ');
                }
                line.pop_back();
                while (line.size() < L) {
                    line.push_back(' ');
                }
            } else {
                // Full justified
                c1 = (L - len) / (j - i - 1);
                c2 = (L - len) % (j - i - 1);
                ci = 0;
                while (true) {
                    line += w[i++];
                    if (i == j) {
                        break;
                    }
                    for (k = 0; k < c1; ++k) {
                        line.push_back(' ');
                    }
                    if (ci < c2) {
                        line.push_back(' ');
                    }
                    ++ci;
                }
            }
            
            res.push_back(line);
        }
        
        return res;
    }
};
