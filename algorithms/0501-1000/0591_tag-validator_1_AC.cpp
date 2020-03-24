// https://discuss.leetcode.com/topic/91381/short-python-accepted-but-not-sure-if-correct
// I don't know how I'm gonna deal with it without using RE matching.
// Don't you think this kind of problems are a bit too complicated?
// Besides, C++ regex is slow.
#include <regex>
#include <string>
using std::regex;
using std::regex_replace;
using std::string;

class Solution {
public:
    bool isValid(string code) {
        if (code == "t") {
            return false;
        }
        
        regex rt("<([A-Z]{1,9})>[^<]*</\\1>");
        regex rc("<!\\[CDATA\\[.*?\\]\\]>");
        string code1;
        
        code = regex_replace(code, rc, "c");
        while (true) {
            code1 = regex_replace(code, rt, "t");
            if (code != code1) {
                code = code1;
            } else {
                break;
            }
        }
        
        return code == "t";
    }
};
