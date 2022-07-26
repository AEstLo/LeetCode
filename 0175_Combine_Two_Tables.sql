-- Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state FROM Person p LEFT JOIN Address a ON p.personId = a.personId;
-- Runtime: 604 ms, faster than 27.77% of MySQL online submissions for Combine Two Tables.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.