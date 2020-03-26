-- https://leetcode.com/problems/students-and-examinations/ 
SELECT stsb.*, 
       COALESCE(exc.attended_exams, 0) attended_exams 
FROM   (SELECT st.student_id, 
               st.student_name, 
               sb.subject_name 
        FROM   students st 
               CROSS JOIN subjects sb) stsb 
       LEFT JOIN (SELECT *, 
                         Count(*) attended_exams 
                  FROM   examinations 
                  GROUP  BY student_id, 
                            subject_name) exc 
              ON stsb.student_id = exc.student_id 
                 AND stsb.subject_name = exc.subject_name 
ORDER  BY stsb.student_id, 
          stsb.subject_name; 
