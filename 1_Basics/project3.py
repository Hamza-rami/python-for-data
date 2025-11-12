from datetime import datetime
import ast

jobs = [
    {"job_title": "Data Analyst", "skills": "['Python', 'Excel', 'SQL', 'Tableau']", "job_date": "2024-11-12"},
    {"job_title": "Data Scientist", "skills": "['Python', 'Pandas', 'Scikit-learn', 'Machine Learning']", "job_date": "2024-12-05"},
    {"job_title": "Business Intelligence Analyst", "skills": "['Power BI', 'SQL', 'Excel', 'DAX']", "job_date": "2025-01-10"},
    {"job_title": "Marketing Analyst", "skills": "['Google Analytics', 'Python', 'Excel', 'Tableau']", "job_date": "2025-01-22"},
    {"job_title": "Financial Analyst", "skills": "['Excel', 'Python', 'VBA', 'SQL']", "job_date": "2024-10-30"},
    {"job_title": "Machine Learning Engineer", "skills": "['Python', 'TensorFlow', 'PyTorch', 'Deep Learning']", "job_date": "2025-02-15"},
    {"job_title": "Data Engineer", "skills": "['Python', 'Spark', 'Hadoop', 'SQL']", "job_date": "2025-03-02"},
    {"job_title": "Quantitative Analyst", "skills": "['Python', 'R', 'Excel', 'Statistics']", "job_date": "2025-01-18"},
    {"job_title": "Healthcare Data Analyst", "skills": "['SQL', 'Python', 'Excel', 'Power BI']", "job_date": "2025-02-05"},
    {"job_title": "Operations Analyst", "skills": "['Excel', 'SQL', 'Python', 'Data Visualization']", "job_date": "2024-12-28"},
    {"job_title": "AI Researcher", "skills": "['Python', 'PyTorch', 'TensorFlow', 'NLP']", "job_date": "2025-01-30"},
    {"job_title": "Risk Analyst", "skills": "['Excel', 'Python', 'Statistics', 'SAS']", "job_date": "2025-02-10"},
    {"job_title": "Data Visualization Specialist", "skills": "['Tableau', 'Power BI', 'Python', 'Excel']", "job_date": "2025-03-12"},
    {"job_title": "Customer Insights Analyst", "skills": "['Excel', 'SQL', 'Python', 'Google Analytics']", "job_date": "2025-02-25"},
    {"job_title": "Big Data Engineer", "skills": "['Hadoop', 'Spark', 'Python', 'Kafka']", "job_date": "2025-03-20"}
]

for job in jobs:
    job["job_date"] = datetime.strptime(job["job_date"], '%Y-%m-%d')
    job["skills"] = ast.literal_eval(job["skills"])
    
print(jobs)