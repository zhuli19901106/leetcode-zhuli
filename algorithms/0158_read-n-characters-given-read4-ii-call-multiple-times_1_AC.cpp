#include <cstring>
using std::memset;

// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    Solution() {
        memset(buf4, 0, (SIZE_BUF + 1) * sizeof(char));
        buf_sz = 0;
        buf_rc = 0;
    }
    
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        if (buf == NULL) {
            return 0;
        }
        if (n <= 0) {
            return 0;
        }
        
        // There's no way to find out if *buf is pointing to a valid area.
        // So let it be, just assume there's enough space for everything.
        
        int bc = 0;
        
        if (buf_rc >= 0) {
            while (bc < n && buf_rc > 0) {
                buf[bc++] = buf4[buf_sz - (buf_rc--)];
            }
        }
        
        while (bc < n) {
            buf_sz = read4(buf4);
            buf_rc = buf_sz;
            if (buf_sz == 0) {
                break;
            }
            
            while (bc < n && buf_rc > 0) {
                buf[bc++] = buf4[buf_sz - (buf_rc--)];
            }
        }
        
        return bc;
    }
private:
    static const int SIZE_BUF = 4;
    
    char buf4[SIZE_BUF + 1];
    int buf_rc;
    int buf_sz;
};
