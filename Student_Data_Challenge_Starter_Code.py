#!/usr/bin/env python
# coding: utf-8

# ### Import required dependencies

# In[503]:


import pandas as pd
import os


# ## Deliverable 1: Collect the Data
# 
# To collect the data that you’ll need, complete the following steps:
# 
# 1. Using the Pandas `read_csv` function and the `os` module, import the data from the `new_full_student_data.csv` file, and create a DataFrame called student_df. 
# 
# 2. Use the head function to confirm that Pandas properly imported the data.
# 

# In[504]:


# Create the path and import the data
import pandas as pd

import os

full_student_data = os.path.join('../Resources/new_full_student_data.csv')

student_df = pd.read_csv(full_student_data)


# In[505]:


# Verify that the data was properly imported
student_df.head()


# ## Deliverable 2: Prepare the Data
# 
# To prepare and clean your data for analysis, complete the following steps:
#     
# 1. Check for and remove all rows with `NaN`, or missing, values in the student DataFrame. 
# 
# 2. Check for and remove all duplicate rows in the student DataFrame.
# 
# 3. Use the `str.replace` function to remove the "th" from the grade levels in the grade column.
# 
# 4. Check data types using the `dtypes` property.
# 
# 5. Remove the "th" suffix from every value in the grade column using `str` and `replace`.
# 
# 6. Change the grade colum to the `int` type and verify column types.
# 
# 7. Use the head (and/or the tail) function to preview the DataFrame.

# In[506]:


# Check for null values

student_df.isnull().sum()


# In[507]:


# Drop rows with null values and verify removal

student_df = student_df.dropna()
student_df.isnull().sum()


# In[508]:


# Check for duplicated rows
student_df.duplicated().sum()


# In[509]:


# Drop duplicated rows and verify removal
student_df = student_df.drop_duplicates()

student_df


# In[510]:


# Check data types
studentids = pd.DataFrame({"student_id"})
studentids.dtypes

names = pd.DataFrame({"student_name"})
names.dtypes

grade = pd.DataFrame({"grade"})
grade.dtypes


# In[511]:


# Examine the grade column to understand why it is not an int

student_df["grade"]= student_df["grade"].str.replace("th", "")


# In[512]:


# Remove the non-numeric characters and verify the contents of the column
student_df.head()


# In[513]:


student_df['grade']


# In[514]:


# Change the grade column to the int type and verify column types
student_df['grade'] = student_df['grade'].astype(int)
student_df.dtypes


# In[515]:


student_df.head()


# ## Deliverable 3: Summarize the Data
# 
# Describe the data using summary statistics on the data as a whole and on individual columns.
# 
# 1. Generate the summary statistics for each DataFrame by using the `describe` function.
# 
# 2. Display the mean math score using the `mean` function. 
# 
# 2. Store the minimum reading score as `min_reading_score`.

# In[516]:


# Display summary statistics for the DataFrame

student_df.describe()


# In[517]:


# Display the mean math score using the mean function

meanmath_df = student_df["math_score"].mean()
meanmath_df


# In[518]:


# Store the minimum reading score as min_reading_score

min_reading_score = student_df["reading_score"].min()

min_reading_score


# ## Deliverable 4: Drill Down into the Data
# 
# Drill down to specific rows, columns, and subsets of the data.
# 
# To drill down into the data, complete the following steps:
# 
# 1. Use `loc` to display the grade column.
# 
# 2. Use `iloc` to display the first 3 rows and columns 3, 4, and 5.
# 
# 3. Show the rows for grade nine using `loc`.
# 
# 4. Store the row with the minimum overall reading score as `min_reading_row` using `loc` and the `min_reading_score` found in Deliverable 3.
# 
# 5. Find the reading scores for the school and grade from the output of step three using `loc` with multiple conditional statements.
# 
# 6. Using conditional statements and `loc` or `iloc`, find the mean reading score for all students in grades 11 and 12 combined.

# In[519]:


# Use loc to display the grade column
student_df.loc[:, ["grade"]]


# In[520]:


# Use `iloc` to display the first 3 rows and columns 3, 4, and 5.
firstrows_df = student_df.iloc[:3, [3, 4, 5]]
firstrows_df


# In[521]:


# Select the rows for grade nine and display their summary statistics using `loc` and `describe`.
grade9_df = student_df.loc[student_df["grade"] == 9]
grade9_df.describe()


# In[522]:


# Store the row with the minimum overall reading score as `min_reading_row`
# using `loc` and the `min_reading_score` found in Deliverable 3.
min_reading_score = student_df["reading_score"].min()
min_reading_row = student_df.loc[student_df["reading_score"] == min_reading_score]
min_reading_row


# In[523]:


# Use loc with conditionals to select all reading scores from 10th graders at Dixon High School.

dixonrdg_df = student_df.loc[(student_df["school_name"] == "Dixon High School") & (student_df["grade"] == 10)]
dixonrdg_df.loc[:,["school_name", "reading_score"]]


# In[524]:


# Find the mean reading score for all students in grades 11 and 12 combined.

student_df.loc[student_df["grade"] > 10, "reading_score"].mean()


# ## Deliverable 5: Make Comparisons Between District and Charter Schools
# 
# Compare district vs charter schools for budget, size, and scores.
# 
# Make comparisons within your data by completing the following steps:
# 
# 1. Using the `groupby` and `mean` functions, look at the average reading and math scores per school type.
# 
# 1. Using the `groupby` and `count` functions, find the total number of students at each school.
# 
# 2. Using the `groupby` and `mean` functions, find the average budget per grade for each school type.

# In[525]:


# Display the average budget for each school type by using the groupby and mean functions

average_budget = student_df.groupby(by='school_type').mean()
average_budget.loc[:, ["school_budget"]]


# In[548]:


# Find the total number of students at each school, and sort those numbers from largest to smallest by using the groupby, count, and sort_values functions
total_students = student_df.groupby(by='school_name').count()
total_students.rename(columns={"student_id":"student_count"}, inplace=True)
total_student_count = total_students[["student_count"]].sort_values("student_count", ascending=False)
total_student_count


# In[540]:


# Find the average math score by grade for each school type by using the groupby and mean functions
avg_math = student_df[['school_type','grade', 'math_score']].groupby(by=['school_type', 'grade'], as_index=True).mean('math_score').round(0)
avg_math


# # Deliverable 6: Summarize Your Findings
# In the cell below, write a few sentences to describe any discoveries you made while performing your analysis along with any additional analysis you believe would be worthwhile.

# *your summary here*

# In[ ]:


# While performing analysis on the student data, I noticed that the average school budgets for public schools is about $40,000 greater than the average budgets for charter schools. This can help inform budgeting needs for schools across districts and can open the department up to conducting further analysis on the reasons behind this difference in funding and whether it makes sense for these different types of schools. Secondly, having access to the number of students at high schools is important data for many different aspects of studying school statistics, including understanding budgets and looking at academic scores. Knowing which schools having higher student populations than others will help in understanding what they need and the progress they make. For example, Montgomery High School has the highest student population at 2038 students, which will mean that their budget, test scores, and needs will look different than Chang High School, which has 171 students. Lastly, being able to look at the average math scores in public and charter schools, and to see these scores by grade, can help the district see where the greatest needs are for math intervention across schools. For example, we can see that 9th grade in charter schools have the highest math scores, but the average math score decreases across charter schools as students advance in high school. This is just one example of an aspect that could merit a deeper dive to understand the why behind these numbers and what can be done to support these students and teachers in increasing scores. 

