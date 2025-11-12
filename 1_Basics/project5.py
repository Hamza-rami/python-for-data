import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#loading data
df = pd.read_csv("/mnt/homes/hrami/Desktop/python/data_jobs.csv")

#data cleanup
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)
fil_salary_year = df['salary_year_avg'].median()
fil_salary_hour = df['salary_hour_avg'].median()

filt_df = df;

filt_df['salary_year_avg'] = filt_df['salary_year_avg'].fillna(fil_salary_year)
filt_df['salary_hour_avg'] = filt_df['salary_hour_avg'].fillna(fil_salary_hour)

filt_df = filt_df.drop_duplicates(subset=['job_title', 'company_name'])
print(filt_df)