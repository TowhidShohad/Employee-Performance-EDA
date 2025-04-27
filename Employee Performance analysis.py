#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
num_employees = 500
employee_ids = np.arange(1, num_employees + 1)
ages = np.random.randint(22, 60, size=num_employees)
departments = np.random.choice(['Sales', 'Marketing', 'IT', 'HR', 'Finance', 'Production'], size=num_employees)
monthly_sales = np.random.uniform(2000, 25000, size=num_employees)
performance_scores = np.random.uniform(1, 10, size=num_employees)

# Create DataFrame
data = {
    'EmployeeID': employee_ids,
    'Age': ages,
    'Department': departments,
    'MonthlySales': monthly_sales,
    'PerformanceScore': performance_scores
}

df = pd.DataFrame(data)
df.head()





# In[4]:


# Task 1: Age Distribution
# Question: What is the distribution of employee ages in the dataset?
# Visualization: Create a histogram or a box plot to visualize the age distribution.

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Number of Employees')
plt.grid(True)
plt.show()

# Alternative visualization - Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Age'])
plt.title('Box Plot of Employee Ages')
plt.show()


# In[5]:


# Task 2: Departmental Distribution
# Question: How are employees distributed across different departments?
# Visualization: Use a bar chart to show the number of employees in each department.

plt.figure(figsize=(8,5))
sns.countplot(x='Department', data=df)
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# In[6]:


# Task 3: Average Performance Score
# Question: Calculate the average performance score across all employees.
# Discussion: Discuss any insights you can derive from the average score.

average_score = df['PerformanceScore'].mean()
print(f"Average Performance Score: {average_score:.2f}")

# Optional: Visualize the distribution of performance scores
plt.figure(figsize=(8,5))
sns.histplot(df['PerformanceScore'], bins=10, kde=True)
plt.title('Distribution of Performance Scores')
plt.xlabel('Performance Score')
plt.ylabel('Number of Employees')
plt.grid(True)
plt.show()


# In[7]:


# Task 4: Sales and Performance Relationship
# Question: Analyze the relationship between monthly sales and performance score.
# Visualization: Create a scatter plot to visualize the relationship.

plt.figure(figsize=(8,5))
sns.scatterplot(x='MonthlySales', y='PerformanceScore', data=df)
plt.title('Monthly Sales vs. Performance Score')
plt.xlabel('Monthly Sales ($)')
plt.ylabel('Performance Score')
plt.grid(True)
plt.show()


# In[8]:


# Task 5: Top-Performing Employees
# Question: Identify the top 5 employees based on performance score.
# Output: Display their details (EmployeeID, Department, MonthlySales, PerformanceScore).

top_performers = df.sort_values(by='PerformanceScore', ascending=False).head(5)
print("Top 5 Performing Employees:")
print(top_performers[['EmployeeID', 'Department', 'MonthlySales', 'PerformanceScore']])


# In[9]:


# Task 6: Departmental Performance Comparison
# Question: Compare the performance scores across different departments.
# Visualization: Use a box plot or bar chart to visualize the differences.

plt.figure(figsize=(10,6))
sns.boxplot(x='Department', y='PerformanceScore', data=df)
plt.title('Performance Score by Department')
plt.xlabel('Department')
plt.ylabel('Performance Score')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[10]:


# Task 7: Average Monthly Sales by Department
# Question: Analyze the average monthly sales by department.
# Visualization: Create a bar chart to display the average sales for each department.

avg_sales_by_dept = df.groupby('Department')['MonthlySales'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,6))
sns.barplot(x=avg_sales_by_dept.index, y=avg_sales_by_dept.values)
plt.title('Average Monthly Sales by Department')
plt.xlabel('Department')
plt.ylabel('Average Monthly Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

print("Average Monthly Sales by Department:")
print(avg_sales_by_dept)


# In[11]:


# Task 8: Monthly Sales and Performance Score Statistics
# Question: Provide summary statistics (mean, median, standard deviation, etc.) for MonthlySales and PerformanceScore.
# Discussion: Include a discussion on the variability and central tendency.

# Summary statistics
summary_stats = df[['MonthlySales', 'PerformanceScore']].describe()
print("Summary Statistics for Monthly Sales and Performance Score:")
print(summary_stats)

# Additional statistics (standard deviation separately)
std_dev = df[['MonthlySales', 'PerformanceScore']].std()
print("\nStandard Deviation:")
print(std_dev)


# In[12]:


# Task 9: Age Statistics
# Question: Calculate the median and interquartile range (IQR) for employee ages.
# Discussion: Discuss any interesting observations about the age distribution.

# Median
median_age = df['Age'].median()

# Interquartile Range (IQR)
q1 = df['Age'].quantile(0.25)
q3 = df['Age'].quantile(0.75)
iqr_age = q3 - q1

print(f"Median Age of Employees: {median_age}")
print(f"Interquartile Range (IQR) of Age: {iqr_age}")

# Optional: Visualizing Age spread
plt.figure(figsize=(6,4))
sns.boxplot(x=df['Age'])
plt.title('Age Spread of Employees')
plt.show()


# In[13]:


# Task 10: Age and Performance Correlation
# Question: Explore the correlation between age and performance score.
# Analysis: Calculate and interpret the correlation coefficient.

correlation_age_perf = df['Age'].corr(df['PerformanceScore'])
print(f"Correlation between Age and Performance Score: {correlation_age_perf:.2f}")

# Interpretation tip:
# Close to 1 → Strong positive correlation
# Close to -1 → Strong negative correlation
# Close to 0 → No or very weak correlation


# In[14]:


# Task 11: Sales and Performance Correlation
# Question: Investigate the correlation between monthly sales and performance score.
# Visualization: Visualize the correlation with a scatter plot and provide interpretation.

# Calculate correlation
correlation_sales_perf = df['MonthlySales'].corr(df['PerformanceScore'])
print(f"Correlation between Monthly Sales and Performance Score: {correlation_sales_perf:.2f}")

# Scatter Plot
plt.figure(figsize=(8,5))
sns.scatterplot(x='MonthlySales', y='PerformanceScore', data=df)
plt.title('Correlation: Monthly Sales vs. Performance Score')
plt.xlabel('Monthly Sales ($)')
plt.ylabel('Performance Score')
plt.grid(True)
plt.show()


# In[15]:


# Task 12: Monthly Sales Distribution
# Question: Create a histogram to visualize the distribution of monthly sales.
# Discussion: Discuss any noticeable patterns or outliers.

plt.figure(figsize=(8,5))
sns.histplot(df['MonthlySales'], bins=15, kde=True)
plt.title('Monthly Sales Distribution')
plt.xlabel('Monthly Sales ($)')
plt.ylabel('Number of Employees')
plt.grid(True)
plt.show()


# In[16]:


# Task 13: Performance Score Spread
# Question: Generate a box plot to show the spread of performance scores across all employees.
# Discussion: Identify any outliers or interesting patterns.

plt.figure(figsize=(8,5))
sns.boxplot(x=df['PerformanceScore'])
plt.title('Spread of Performance Scores')
plt.xlabel('Performance Score')
plt.grid(True)
plt.show()


# In[17]:


# Task 14: Departmental Performance Comparison (Bar Chart)
# Question: Plot a bar chart comparing performance scores across departments.
# Highlight any departments that stand out in terms of performance.

# Calculate average performance score by department
avg_perf_by_dept = df.groupby('Department')['PerformanceScore'].mean().sort_values(ascending=False)

# Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(x=avg_perf_by_dept.index, y=avg_perf_by_dept.values)
plt.title('Average Performance Score by Department')
plt.xlabel('Department')
plt.ylabel('Average Performance Score')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

print("Average Performance Score by Department:")
print(avg_perf_by_dept)

