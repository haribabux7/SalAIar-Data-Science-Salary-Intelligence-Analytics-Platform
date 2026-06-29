-- SQL EDA & Business Analysis for DS Salaries

-- 1. Dataset Summary
SELECT 
    COUNT(*) as total_records,
    COUNT(DISTINCT job_title) as unique_jobs,
    AVG(salary_in_usd) as avg_salary,
    MIN(salary_in_usd) as min_salary,
    MAX(salary_in_usd) as max_salary
FROM ds_salaries;

-- 2. Category Analysis (Experience Level)
SELECT 
    experience_level, 
    AVG(salary_in_usd) as avg_salary,
    COUNT(*) as job_count
FROM ds_salaries
GROUP BY experience_level
ORDER BY avg_salary DESC;

-- 3. Trend Analysis (Yearly Growth)
SELECT 
    work_year, 
    AVG(salary_in_usd) as avg_salary
FROM ds_salaries
GROUP BY work_year
ORDER BY work_year;

-- 4. Top 5 Highest Paying Job Titles
SELECT 
    job_title, 
    AVG(salary_in_usd) as avg_salary
FROM ds_salaries
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 5;

-- 5. Segmentation (Company Size)
SELECT 
    company_size, 
    AVG(salary_in_usd) as avg_salary,
    COUNT(*) as count
FROM ds_salaries
GROUP BY company_size;
