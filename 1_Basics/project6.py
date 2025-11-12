import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#loading data
df = pd.read_csv("/mnt/homes/hrami/Desktop/python/data_jobs.csv")

#data cleanup
df['job_posted_date'] = pd.to_datetime(df.job_posted_date)

df.sample()