// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        static const int N = 4;
        
        if (buf == NULL) {
            return 0;
        }
        
        char c[N + 1];
        int i, j;
        int cc;
        
        i = 0;
        while (i < n) {
            cc = read4(c);
            j = 0;
            while (i < n && j < cc) {
                buf[i++] = c[j++];
            }
            if (cc < N) {
                break;
            }
        }
        return i;
    }
};
