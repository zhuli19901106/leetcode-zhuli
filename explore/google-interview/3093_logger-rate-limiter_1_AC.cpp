class Logger {
public:
    /** Initialize your data structure here. */
    Logger() {
        cur_time = 0;
        gc_time = TIME_GC;
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        // Let's suppose timestamp never goes backward.
        cur_time = timestamp;
        if (cur_time >= gc_time) {
            // Do some garbage collection
            gc();
        }
        
        bool res = !(um.find(message) != um.end() && um[message] > timestamp - 
            TIME_EXPIRE);
        if (res) {
            um[message] = timestamp;
        }
        return res;
    }
    
    ~Logger() {
        um.clear();
    }
private:
    static const int TIME_EXPIRE = 10;
    static const int TIME_GC = 100;
    
    unordered_map<string, int> um;
    int cur_time;
    int gc_time;
    
    void gc() {
        gc_time = (cur_time + (TIME_GC - 1)) / TIME_GC * TIME_GC;
        auto it = um.begin();
        while (it != um.end()) {
            if (it->second <= cur_time - TIME_EXPIRE) {
                it = um.erase(it);
            } else {
                ++it;
            }
        }
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.shouldPrintMessage(timestamp,message);
 */
