# 📊 Data Analyst Job Market Analysis

This project analyzes **data analyst job postings** to uncover trends in:
- Skill demand 📈  
- Salary distribution 💵  
- Remote work and benefits 💼  

Inspired by **Luke Barousse’s Data Analyst Portfolio Project**, this repository visualizes insights using Python, Pandas, and Matplotlib.

---

## 🧠 Objectives

1. Identify top in-demand and highest-paying skills for Data Analysts  
2. Compare job benefits such as remote work and health insurance  
3. Track changes in skill demand across months  

---

## 🧰 Tools Used

- **Python**
- **Pandas** for data manipulation  
- **Matplotlib** / **Seaborn** for visualization  
- **Jupyter Notebook** for analysis  

---

## 📈 1. Top 6 Skills for Data Analysts per Month

This chart shows how demand for the top 6 skills changes monthly.

```python
import matplotlib.pyplot as plt
import seaborn as sns

top6 = df[df['job_title_short'] == 'Data Analyst']
top6 = top6.groupby(['Month', 'job_skills']).size().reset_index(name='count')
top6 = top6[top6['job_skills'].isin(['sql', 'excel', 'python', 'tableau', 'power bi', 'r'])]

sns.lineplot(data=top6, x='Month', y='count', hue='job_skills', style='job_skills',
             markers=True, dashes=True)
plt.title("Top 6 skills for Data Analysts per month")
plt.show()
```
## 🏠 2. Job Benefits Distribution

In this section, we explore the **benefits** offered in Data Analyst job postings.  
We’ll analyze how often companies mention **remote work**, **no degree requirement**, and **health insurance** benefits.  

These insights help understand how the job market supports **work-life balance** and **accessibility** for candidates.

---

### 📊 Visualization Code

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

# Work from Home
df['job_work_from_home'].value_counts().plot(
    kind='pie',
    ax=ax[0],
    autopct='%1.2f%%',
    colors=['#1f77b4', '#ff7f0e'],
    title='Work from Home Status'
)

# No Degree Mention
df['job_no_degree_mention'].value_counts().plot(
    kind='pie',
    ax=ax[1],
    autopct='%1.2f%%',
    colors=['#1f77b4', '#ff7f0e'],
    title='No Degree Mention'
)

# Health Insurance
df['job_health_insurance'].value_counts().plot(
    kind='pie',
    ax=ax[2],
    autopct='%1.2f%%',
    colors=['#1f77b4', '#ff7f0e'],
    title='Health Insurance'
)

plt.tight_layout()
plt.show()
```
## 💰 3. Top 10 Highest-Paying and Most In-Demand Skills for Data Analysts

This section compares which **skills bring the highest salaries** and which are **most requested** in job postings.  
It helps highlight where to focus learning efforts — balancing *demand* and *earning potential*.

---

### 📊 Visualization Code

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 1, figsize=(8, 6))

# --- Top 10 Highest-Paying Skills ---
df_salary = (
    df.groupby('job_skills')['median_salary']
      .median()
      .nlargest(10)
      .sort_values()
)
df_salary.plot(kind='barh', ax=ax[0], color='steelblue')
ax[0].set_title('Top 10 Highest-Pay Skills for Data Analyst')
ax[0].set_xlabel('Median Salary ($USD)')

# --- Top 10 Most In-Demand Skills ---
df_demand = (
    df['job_skills']
      .value_counts()
      .nlargest(10)
      .sort_values()
)
df_demand.plot(kind='barh', ax=ax[1], color='cornflowerblue')
ax[1].set_title('Top 10 Most In-Demand Skills for Data Analyst')
ax[1].set_xlabel('Number of Job Postings')

plt.tight_layout()
plt.show()
```
## 🧭 5. Conclusion

This project was an incredible learning experience that combined **data analysis**, **Python programming**, and **data visualization**.

By exploring real job posting data, I learned how to:
- Use **Pandas** to clean and group data  
- Use **Matplotlib** and **Seaborn** to build meaningful visualizations  
- Interpret data insights to understand **real-world job trends**

---

### 🧩 Key Takeaways

- **SQL**, **Python**, and **Excel** are the foundation of most Data Analyst roles.  
- Visualization tools like **Power BI** and **Tableau** remain highly valuable.  
- Companies are increasingly open to candidates **without formal degrees**, focusing on skills.  
- Remote opportunities are growing but still represent a small share of the total market.

---

## 🧠 7. About This Project
This project is based on Luke Barousse’s YouTube Data Analyst Portfolio Project, recreated as a personal learning exercise.

It helped me understand how to:
- Work with real-world job data
- Build a professional data analytics portfolio project
- Present findings in a clear, visual, and professional format
I’m still learning and improving my skills in:
- Data Cleaning
- Visualization Design
- Communication of Insights

If you have feedback or suggestions, I’d love to hear them!

## 👤 About Me

Hi! I’m Hamza Rami — a beginner Data Analyst passionate about learning how to turn data into insights.

This is my first full data analytics project, built while following Luke Barousse’s tutorial.
