import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#loading data
df = pd.read_csv("/mnt/homes/hrami/Desktop/python/data_jobs.csv")

#data cleanup
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

# us_jobs = df[df['job_country'] == "United States"]
# us_jobs = us_jobs[us_jobs['salary_year_avg'].notna()]

# job_posted_month = df['job_posted_date'].dt.month
# monthly_counts = job_posted_month.value_counts()
# monthly_counts = monthly_counts.sort_index()

median_sal = df.groupby('job_title_short')['salary_year_avg'].median()
median_sal = median_sal.sort_values()
plt.barh(median_sal.index, median_sal)
plt.title('median salary by job title')
plt.xlabel("salary ($USD)")
plt.show()