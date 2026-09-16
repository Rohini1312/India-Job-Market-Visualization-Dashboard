import pandas as pd
import random

random.seed(42)

companies = [
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Deloitte",
    "Capgemini",
    "Tech Mahindra",
    "Cognizant",
    "HCL Technologies",
    "IBM"
]

locations = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Pune",
    "Mumbai",
    "Delhi",
    "Noida"
]

job_titles = [
    "Data Analyst",
    "Python Developer",
    "Data Scientist",
    "Software Engineer",
    "Machine Learning Engineer",
    "Business Analyst",
    "Web Developer"
]

skills = [
    "Python",
    "SQL",
    "Excel",
    "Power BI",
    "Machine Learning",
    "Java",
    "Tableau"
]

job_types = [
    "Full-time",
    "Part-time",
    "Internship"
]

experience_levels = [
    "0-1 Years",
    "1-3 Years",
    "3-5 Years",
    "5+ Years"
]

data = []

for i in range(200):

    job = {
        "Job_ID": f"JOB{i+1:03d}",
        "Job_Title": random.choice(job_titles),
        "Company": random.choice(companies),
        "Location": random.choice(locations),
        "Skill": random.choice(skills),
        "Job_Type": random.choice(job_types),
        "Experience": random.choice(experience_levels),
        "Salary_LPA": random.randint(3, 20)
    }

    data.append(job)

df = pd.DataFrame(data)

df.to_csv(
    "data/india_job_market.csv",
    index=False
)

print("Dataset created successfully!")
print("Total records:", len(df))

print("\nFirst 5 records:")
print(df.head())