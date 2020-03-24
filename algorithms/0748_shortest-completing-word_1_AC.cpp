// Due to the extremely short length of words, brute-force seems to be sufficient.
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
using std::islower;
using std::isupper;
using std::memset;
using std::string;
using std::vector;

class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
		string res = "";
		bool found = false;
		for (auto &w: words) {
			if (!contain(w, licensePlate)) {
				continue;
			}
			if (!found || res.size() > w.size()) {
				found = true;
				res = w;
			}
		}
		return res;
    }
private:
	bool contain(const string &s1, const string &s2) {
		const int N = 26;
		int c1[N], c2[N];
		
		memset(c1, 0, N * sizeof(int));
		memset(c2, 0, N * sizeof(int));
		
		for (auto &c: s1) {
			if (isupper(c)) {
				++c1[c - 'A'];
			} else if (islower(c)) {
				++c1[c - 'a'];
			}
		}
		for (auto &c: s2) {
			if (isupper(c)) {
				++c2[c - 'A'];
			} else if (islower(c)) {
				++c2[c - 'a'];
			}
		}
		
		int i;
		for (i = 0; i < N; ++i) {
			if (c1[i] < c2[i]) {
				return false;
			}
		}
		return true;
	}
};
