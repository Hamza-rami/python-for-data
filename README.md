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
df_da = df[df['job_title_short'] == 'Data Analyst'].copy()

df_da['job_posted_month_no'] = df_da['job_posted_date'].dt.month
df_da_explode = df_da.explode('job_skills')
df_da_pivot = df_da_explode.pivot_table(index='job_posted_month_no', columns='job_skills', aggfunc='size', fill_value=0)
df_da_pivot.loc['Total'] = df_da_pivot.sum()
df_da_pivot = df_da_pivot[df_da_pivot.loc['Total'].sort_values(ascending=False).index]
df_da_pivot = df_da_pivot.drop('Total')

df_da_pivot.iloc[:,:6].plot(
    kind="line",
    linewidth=4,
    linestyle='--', # more option
    colormap='plasma', # more option
    marker="o", # more option
    markersize=6,
    figsize=(10,8)

)
plt.title('top 6 skills for Data analysts per month')
plt.ylabel('count')
plt.xlabel('Month')
plt.show()
```
![Alt text](Screenshot%20from%202025-11-12%2003-07-06.png)

## 🏠 2. Job Benefits Distribution

In this section, we explore the **benefits** offered in Data Analyst job postings.  
We’ll analyze how often companies mention **remote work**, **no degree requirement**, and **health insurance** benefits.  

These insights help understand how the job market supports **work-life balance** and **accessibility** for candidates.

---

### 📊 Visualization Code

```python
fig, ax = plt.subplots(1, 3)
dict = {'job_work_from_home':'Work from Home Status', 'job_no_degree_mention': 'No Degree Mention', 'job_health_insurance':'Health Insurance'}

for i, (colum, title) in enumerate(dict.items()):
    df[colum].value_counts().plot(
        kind='pie', 
        startangle=45, 
        autopct='%1.2f%%', 
        title=title, 
        ax=ax[i]
    )

fig.tight_layout()
fig.set_size_inches(15, 8)
```
![Alt text](Screenshot%20from%202025-11-12%2003-07-49.png)

## 💰 3. Top 10 Highest-Paying and Most In-Demand Skills for Data Analysts

This section compares which **skills bring the highest salaries** and which are **most requested** in job postings.  
It helps highlight where to focus learning efforts — balancing *demand* and *earning potential*.

---

### 📊 Visualization Code

```python
fig, ax = plt.subplots(2, 1)

df_most_pay.plot(kind='barh',y='median', ax=ax[0], legend=False)
ax[0].invert_yaxis()
ax[0].set_title('Top 10 highest pay skills for Data analyst')
ax[0].set_ylabel("")
ax[0].set_xlabel("")
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _:f'${int(x/1000)}K'))
df_most_skills.plot(kind='barh',y='median', ax=ax[1], legend=False)
ax[1].invert_yaxis()
ax[1].set_xlim(ax[0].get_xlim())
ax[1].set_title('Top 10 Most in demand skills for Data analyst')
ax[1].set_ylabel("")
ax[1].set_xlabel("Median Salary ($USD)")
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _:f'${int(x/1000)}K'))
fig.tight_layout()
```
![Alt text](/Screenshot%20from%202025-11-12%2003-08-42.png)

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
