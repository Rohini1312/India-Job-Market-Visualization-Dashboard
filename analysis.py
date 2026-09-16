import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_job_market.csv")

print("=" * 60)
print("        INDIA JOB MARKET ANALYSIS")
print("=" * 60)

# Total jobs
print("\nTotal Jobs:", len(df))

# Jobs by location
print("\n--- Jobs by Location ---")
print(df["Location"].value_counts())

# Jobs by company
print("\n--- Jobs by Company ---")
print(df["Company"].value_counts())

# Jobs by job title
print("\n--- Jobs by Job Title ---")
print(df["Job_Title"].value_counts())

# Jobs by skill
print("\n--- Jobs by Skill ---")
print(df["Skill"].value_counts())

# Jobs by experience
print("\n--- Jobs by Experience ---")
print(df["Experience"].value_counts())

# Jobs by job type
print("\n--- Jobs by Job Type ---")
print(df["Job_Type"].value_counts())

# Salary statistics
print("\n--- Salary Statistics ---")
print(df["Salary_LPA"].describe())

# Average salary
average_salary = df["Salary_LPA"].mean()

print("\nAverage Salary:", round(average_salary, 2), "LPA")

# Highest salary
print("Highest Salary:", df["Salary_LPA"].max(), "LPA")

# Lowest salary
print("Lowest Salary:", df["Salary_LPA"].min(), "LPA")

print("\n" + "=" * 60)
print("Analysis completed successfully!")
print("=" * 60)