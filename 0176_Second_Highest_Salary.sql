-- Write your MySQL query statement below
SELECT IFNULL((SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1), NULL) AS SecondHighestSalary;
-- Runtime: 238 ms, faster than 65.59% of MySQL online submissions for Second Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.