// Base64 is an option.
#include <cctype>
#include <string>
#include <vector>
using std::isdigit;
using std::string;
using std::to_string;
using std::vector;

class Codec {
public:
    Codec() {
        b64 = "";
        bi.resize(SIZE_DICT, -1);
        
        int idx = 0;
        int i;
        for (i = 0; i < 26; ++i) {
            b64.push_back('A' + i);
            bi['A' + i] = idx++;
        }
        for (i = 0; i < 26; ++i) {
            b64.push_back('a' + i);
            bi['a' + i] = idx++;
        }
        for (i = 0; i < 10; ++i) {
            b64.push_back('0' + i);
            bi['0' + i] = idx++;
        }
        b64.push_back('+');
        bi['+'] = idx++;
        b64.push_back('/');
        bi['/'] = idx++;
    }
    
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        auto &a = strs;
        int n = a.size();
        string res = "";
        
        res.push_back(CHAR_SEQ_DEL);
        for (auto &s: a) {
            res += encodeSingle(s);
        }
        res.push_back(CHAR_SEQ_DEL);
        
        return res;
    }
    
    string encodeSingle(string &s) {
        string t = encodeBase64(s);
        int lt = t.size();
        
        string res = "";
        
        res.push_back(CHAR_WORD_DEL);
        res += to_string(lt);
        res.push_back(CHAR_WORD_DEL);
        res += t;
        res.push_back(CHAR_WORD_DEL);
        
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res;
        int ls = s.size();
        if (!(ls >= 2 && s[0] == CHAR_SEQ_DEL && s[ls - 1] == CHAR_SEQ_DEL)) {
            return res;
        }
        int i, j;
        string ss;
        
        i = 1;
        while (i < ls - 1) {
            j = i + 1;
            while (j < ls - 1 && s[j] != CHAR_WORD_DEL) {
                ++j;
            }
            ++j;
            while (j < ls - 1 && s[j] != CHAR_WORD_DEL) {
                ++j;
            }
            ++j;
            ss = s.substr(i, j - i);
            res.push_back(decodeSingle(ss));
            i = j;
        }
        
        return res;
    }
    
    string decodeSingle(string &s) {
        string res = "";
        int ls = s.size();
        if (!(ls >= 2 && s[0] == CHAR_WORD_DEL && s[ls - 1] == CHAR_WORD_DEL)) {
            return res;
        }
        
        int i = 1;
        int lt = 0;
        while (i < ls && isdigit(s[i])) {
            lt = lt * 10 + (s[i] - '0');
            ++i;
        }
        ++i;
        
        string t = s.substr(i, ls - 1 - i);
        if (t.size() != lt) {
            return res;
        }
        
        return decodeBase64(t);
    }
    
    ~Codec() {
        b64.clear();
        bi.clear();
    }
private:
    static const int SIZE_DICT = 256;
    // Make sure the delimiter you choose is not among the charset of the encoding/decoding scheme.
    // Otherwise you'll have to use escaped charaters to avoid ambiguity.
    static const char CHAR_WORD_DEL = '\0';
    static const char CHAR_SEQ_DEL = '\1';
    
    string b64;
    vector<int> bi;
    
    string encodeBase64(string &s) {
        // Any implementation is OK, base64 is just one option.
        int ls = s.size();
        string t = "";
        int i;
        int idx;
        int val;
        int bc;
        
        val = 0;
        bc = 0;
        i = 0;
        do {
            val = (val << 8) + s[i++];
            bc += 8;
            while (bc >= 6) {
                idx = (val >> bc - 6);
                val &= (1 << bc - 6) - 1;
                t.push_back(b64[idx]);
                
                bc -= 6;
            }
        } while (i < ls);
        if (bc > 0) {
            val <<= (6 - bc);
            idx = val;
            t.push_back(b64[idx]);
            
            bc = 0;
        }
        
        // Padding with '=' is unnecessary if you got other delimiters in place.
        return t;
    }
    
    string decodeBase64(string &s) {
        // Any implementation is OK, base64 is just one option.
        int ls = s.size();
        string t = "";
        int i;
        int idx;
        int val;
        int bc;
        
        val = 0;
        bc = 0;
        i = 0;
        do {
            val = (val << 6) + bi[s[i++]];
            bc += 6;
            while (bc >= 8) {
                idx = (val >> (bc - 8));
                val &= (1 << (bc - 8)) - 1;
                t.push_back(idx);
                
                bc -= 8;
            }
        } while (i < ls);
        return t;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
