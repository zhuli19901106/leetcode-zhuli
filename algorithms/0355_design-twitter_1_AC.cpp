// This is a system design problem, right?
// Suppose every "ID" here is globally unique, alright?
// Otherwise it's not an ID afterall.
// Seriously, you're gonna solve this problem within 30 minutes?
// I don't think I can make it.
#include <cstdint>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::priority_queue;
using std::unordered_map;
using std::unordered_set;
using std::vector;

// For real, there should be a real timer, not just a counter.
static int64_t timestamp_counter = 0;
static const int NUM_RECENT_TWEETS = 10;

typedef struct Tweet {
    int id;
    int user_id;
    int64_t timestamp;
    
    Tweet(int _id = 0, int _user_id = 0): id(_id), user_id(_user_id) {
        timestamp = ++timestamp_counter;
    }
} Tweet;

typedef struct User {
    int id;
    unordered_set<int> tweets;
    unordered_set<int> fans;
    unordered_set<int> follows;
    vector<int> recent_tweets;
    
    User(int _id = 0): id(_id) {
        fans.insert(id);
        follows.insert(id);
    }
    
    ~User() {
        tweets.clear();
        fans.clear();
        follows.clear();
        recent_tweets.clear();
    }
} User;

typedef struct RecentTweet {
    User *user;
    int idx;
    int64_t timestamp;
    
    RecentTweet(User *_user = NULL, int _idx = 0, int _timestamp = 0): 
        user(_user), idx(_idx), timestamp(_timestamp) {}
} RecentTweet;

typedef struct TopfeedsComparator {
    bool operator () (const RecentTweet &p1, const RecentTweet &p2) {
        return p1.timestamp < p2.timestamp;
    }
} TopfeedsComparator;

class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter() {}
    
    /** Compose a new tweet. */
    void postTweet(int user_id, int tweet_id) {
        checkUser(user_id);
        
        auto &user = list_user[user_id];
        list_tweet[tweet_id] = Tweet(tweet_id, user_id);
        user.tweets.insert(tweet_id);
        
        if (NUM_RECENT_TWEETS <= 0) {
            return;
        }
        
        while (user.recent_tweets.size() >= NUM_RECENT_TWEETS) {
            user.recent_tweets.erase(user.recent_tweets.begin());
        }
        user.recent_tweets.push_back(tweet_id);
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int user_id) {
        checkUser(user_id);
        
        vector<int> top_feeds;
        priority_queue<RecentTweet, vector<RecentTweet>, TopfeedsComparator> pq;
        RecentTweet p;
        User *u1;
        
        u1 = &list_user[user_id];
        for (auto it = u1->follows.begin(); it != u1->follows.end(); ++it) {
            p.user = &list_user[(*it)];
            if (p.user->recent_tweets.size() == 0) {
                continue;
            }
            p.idx = p.user->recent_tweets.size() - 1;
            p.timestamp = list_tweet[p.user->recent_tweets[p.idx]].timestamp;
            pq.push(p);
        }
        
        while (!pq.empty() && top_feeds.size() < NUM_RECENT_TWEETS) {
            p = pq.top();
            pq.pop();
            
            top_feeds.push_back(p.user->recent_tweets[p.idx]);
            --p.idx;
            
            if (p.idx < 0) {
                continue;
            }
            p.timestamp = list_tweet[p.user->recent_tweets[p.idx]].timestamp;
            pq.push(p);
        }
        while (!pq.empty()) {
            pq.pop();
        }
        return top_feeds;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int follower_id, int followee_id) {
        if (follower_id == followee_id) {
            return;
        }
        checkUser(follower_id);
        checkUser(followee_id);
        
        auto &follower = list_user[follower_id];
        auto &followee = list_user[followee_id];
        follower.follows.insert(followee_id);
        followee.fans.insert(follower_id);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int follower_id, int followee_id) {
        if (follower_id == followee_id) {
            return;
        }
        checkUser(follower_id);
        checkUser(followee_id);
        
        auto &follower = list_user[follower_id];
        auto &followee = list_user[followee_id];
        if (follower.follows.find(followee_id) != follower.follows.end()) {
            follower.follows.erase(followee_id);
        }
        if (followee.fans.find(follower_id) != followee.fans.end()) {
            followee.fans.erase(follower_id);
        }
    }
    
    ~Twitter() {
        list_tweet.clear();
        list_user.clear();
    }
private:
    unordered_map<int, Tweet> list_tweet;
    unordered_map<int, User> list_user;
    
    void checkUser(int user_id) {
        if (list_user.find(user_id) != list_user.end()) {
            return;
        }
        list_user[user_id] = User(user_id);
    }
};
