-- https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/ 
-- 1AC, count / count
SELECT Round(Ifnull((SELECT Count(DISTINCT requester_id, accepter_id) 
                     FROM   request_accepted) / (SELECT 
                           Count(DISTINCT sender_id, send_to_id) 
                                                 FROM   friend_request), 0), 2) 
       accept_rate; 
