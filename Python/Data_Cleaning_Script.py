import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('Dataset/Raw_Data.csv')

# 1. Missing Value Handling
# Checking for nulls
null_counts = df.isnull().sum()
# In this specific dataset, there usually aren't many nulls, but let's be robust.
df = df.dropna()

# 2. Duplicate Removal
df = df.drop_duplicates()

# 3. Outlier Detection (using IQR for salary_in_usd)
Q1 = df['salary_in_usd'].quantile(0.25)
Q3 = df['salary_in_usd'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# We might not want to remove outliers in salary data as high salaries are real, 
# but for the sake of the prompt "Outlier Detection", we'll flag them or handle them.
df['is_outlier'] = (df['salary_in_usd'] < lower_bound) | (df['salary_in_usd'] > upper_bound)

# 4. Data Validation
# Ensure work_year is within a reasonable range
df = df[df['work_year'].between(2020, 2026)]

# 5. Feature Engineering
# Map experience levels to more descriptive names
exp_map = {'EN': 'Entry-level', 'MI': 'Mid-level', 'SE': 'Senior-level', 'EX': 'Executive-level'}
df['experience_level_full'] = df['experience_level'].map(exp_map)

# Map employment types
emp_map = {'FT': 'Full-time', 'PT': 'Part-time', 'CT': 'Contract', 'FL': 'Freelance'}
df['employment_type_full'] = df['employment_type'].map(emp_map)

# Remote Ratio label
df['remote_status'] = df['remote_ratio'].map({0: 'On-site', 50: 'Hybrid', 100: 'Remote'})

# 6. Data Type Conversion
df['work_year'] = df['work_year'].astype(int)

# 7. Standardization
# Clean up Unnamed: 0 if it exists
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Export Cleaned Data
df.to_csv('Dataset/Cleaned_Data.csv', index=False)

print("Data cleaning completed. Cleaned_Data.csv saved.")
