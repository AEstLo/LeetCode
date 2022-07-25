-- Write your MySQL query statement below
SELECT class FROM Courses GROUP BY class HAVING COUNT(student) >= 5;

-- Runtime: 307 ms, faster than 63.44% of MySQL online submissions for Classes More Than 5 Students.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Classes More Than 5 Students.