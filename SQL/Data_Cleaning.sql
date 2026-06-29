-- SQL Data Cleaning Script for DS Salaries Dataset

-- 1. Create Table (Assuming CSV is imported into a staging table)
-- CREATE TABLE ds_salaries_staging (...);

-- 2. Handle Missing Values
-- Check for nulls
SELECT COUNT(*) FROM ds_salaries_staging WHERE job_title IS NULL OR salary_in_usd IS NULL;

-- 3. Remove Duplicates
-- Use a CTE to identify and delete duplicates
WITH CTE AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY work_year, experience_level, employment_type, job_title, salary_in_usd, employee_residence, remote_ratio, company_location, company_size
               ORDER BY (SELECT NULL)
           ) as row_num
    FROM ds_salaries_staging
)
DELETE FROM CTE WHERE row_num > 1;

-- 4. Feature Engineering: Experience Level mapping
ALTER TABLE ds_salaries_staging ADD COLUMN experience_level_full VARCHAR(50);
UPDATE ds_salaries_staging 
SET experience_level_full = CASE 
    WHEN experience_level = 'EN' THEN 'Entry-level'
    WHEN experience_level = 'MI' THEN 'Mid-level'
    WHEN experience_level = 'SE' THEN 'Senior-level'
    WHEN experience_level = 'EX' THEN 'Executive-level'
END;

-- 5. Feature Engineering: Remote Ratio mapping
ALTER TABLE ds_salaries_staging ADD COLUMN remote_status VARCHAR(20);
UPDATE ds_salaries_staging 
SET remote_status = CASE 
    WHEN remote_ratio = 0 THEN 'On-site'
    WHEN remote_ratio = 50 THEN 'Hybrid'
    WHEN remote_ratio = 100 THEN 'Remote'
END;

-- 6. Outlier Flagging
ALTER TABLE ds_salaries_staging ADD COLUMN is_outlier BOOLEAN DEFAULT FALSE;
-- (Implementation depends on the specific SQL dialect for calculating quartiles)

-- 7. Standardizing Country Codes (Example)
UPDATE ds_salaries_staging SET company_location = UPPER(company_location);
