-- Run as a MySQL administrator. Replace the username, password and host.
-- This account is intended for the Enterprise Knowledge Copilot SQL agent.
CREATE USER IF NOT EXISTS 'copilot_reader'@'%' IDENTIFIED BY 'REPLACE_WITH_A_LONG_RANDOM_PASSWORD';

-- Grant read access only to the employee table in the attrition database.
GRANT SELECT ON employee_attrition_db.employees
TO 'copilot_reader'@'%';

-- Verify the resulting privileges.
SHOW GRANTS FOR 'copilot_reader'@'%';

-- Do not grant INSERT, UPDATE, DELETE, CREATE, ALTER, DROP or FILE privileges.
