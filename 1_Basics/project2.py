my_skils = ["Python", "Excel", "SQL"]


data_jobs = [
    {
        "jobs": "Data Analyst",
        "skills": ["Python", "Excel", "SQL", "Pandas", "Matplotlib", "Seaborn", "Statistics", "Data Cleaning", "Reporting"]
    },
    {
        "jobs": "Business Analyst",
        "skills": ["Excel", "SQL", "Power BI / Tableau", "Data Visualization", "Communication", "Critical Thinking"]
    },
    {
        "jobs": "Data Scientist",
        "skills": ["Python", "R", "SQL", "Machine Learning", "Statistics", "Data Visualization", "Pandas", "NumPy", "Scikit-learn"]
    },
    {
        "jobs": "Data Engineer",
        "skills": ["Python", "SQL", "ETL", "Big Data (Hadoop, Spark)", "Database Management", "Airflow", "Data Warehousing"]
    },
    {
        "jobs": "Business Intelligence (BI) Developer",
        "skills": ["SQL", "Power BI", "Tableau", "Data Modeling", "ETL", "Excel"]
    },
    {
        "jobs": "Machine Learning Engineer",
        "skills": ["Python", "TensorFlow / PyTorch", "Machine Learning Algorithms", "Data Preprocessing", "SQL", "Statistics"]
    },
    {
        "jobs": "Data Visualization Specialist",
        "skills": ["Tableau / Power BI", "Excel", "Python (Matplotlib, Seaborn)", "Data Storytelling", "Design Principles"]
    },
    {
        "jobs": "Marketing Analyst",
        "skills": ["Excel", "SQL", "Python", "Google Analytics", "Data Visualization", "Statistics"]
    },
    {
        "jobs": "Financial Data Analyst",
        "skills": ["Excel", "SQL", "Python", "Statistics", "Financial Modeling", "Data Cleaning", "Data Visualization"]
    }
]

qualified_jobs = []

for job in data_jobs:
    match = True
    for i in range(3):
        if my_skils[i] not in job["skills"]:
            match = False
            break
    if match:
        qualified_jobs.append(job["jobs"])
print("Qualified Jobs:", qualified_jobs)
