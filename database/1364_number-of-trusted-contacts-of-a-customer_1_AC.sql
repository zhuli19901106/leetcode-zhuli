-- https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/
-- 1AC, you trying to kill me?
SELECT icn.invoice_id, 
       icn.customer_name, 
       icn.price, 
       Ifnull(ctc_cttc.contacts_cnt, 0)         contacts_cnt, 
       Ifnull(ctc_cttc.trusted_contacts_cnt, 0) trusted_contacts_cnt 
FROM   (SELECT i.invoice_id, 
               i.price, 
               i.user_id, 
               cu.customer_name 
        FROM   invoices i 
               LEFT JOIN customers cu 
                      ON i.user_id = cu.customer_id) icn 
       LEFT JOIN (SELECT ctc.user_id, 
                         ctc.contacts_cnt                     contacts_cnt, 
                         Ifnull(cttc.trusted_contacts_cnt, 0) 
                         trusted_contacts_cnt 
                  FROM   (SELECT user_id, 
                                 Count(contact_email) contacts_cnt 
                          FROM   contacts 
                          GROUP  BY user_id) ctc 
                         LEFT JOIN (SELECT user_id, 
                                           Count(contact_email) 
                                           trusted_contacts_cnt 
                                    FROM   contacts 
                                    WHERE  contact_email IN (SELECT email 
                                                             FROM   customers) 
                                    GROUP  BY user_id) cttc 
                                ON ctc.user_id = cttc.user_id) ctc_cttc 
              ON icn.user_id = ctc_cttc.user_id 
ORDER  BY icn.invoice_id; 
