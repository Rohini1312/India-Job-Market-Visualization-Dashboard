import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
df = pd.read_csv("data/cleaned_job_market.csv")

# Make sure output folder exists
os.makedirs("output", exist_ok=True)

# --------------------------------
# 1. Jobs by Location
# --------------------------------

location = df["Location"].value_counts()

plt.figure(figsize=(10, 5))
location.plot(kind="bar")
plt.title("Jobs by Location")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/jobs_by_location.png")
plt.close()


# --------------------------------
# 2. Jobs by Company
# --------------------------------

company = df["Company"].value_counts()

plt.figure(figsize=(10, 5))
company.plot(kind="bar")
plt.title("Jobs by Company")
plt.xlabel("Company")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/jobs_by_company.png")
plt.close()


# --------------------------------
# 3. Jobs by Skill
# --------------------------------

skill = df["Skill"].value_counts()

plt.figure(figsize=(10, 5))
skill.plot(kind="bar")
plt.title("Most Demanded Skills")
plt.xlabel("Skill")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/jobs_by_skill.png")
plt.close()


# --------------------------------
# 4. Jobs by Experience
# --------------------------------

experience = df["Experience"].value_counts()

plt.figure(figsize=(8, 5))
experience.plot(kind="bar")
plt.title("Jobs by Experience Level")
plt.xlabel("Experience")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/jobs_by_experience.png")
plt.close()


# --------------------------------
# 5. Jobs by Job Type
# --------------------------------

job_type = df["Job_Type"].value_counts()

plt.figure(figsize=(8, 6))
job_type.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Jobs by Job Type")
plt.ylabel("")
plt.tight_layout()
plt.savefig("output/jobs_by_type.png")
plt.close()


# --------------------------------
# 6. Average Salary by Location
# --------------------------------

salary = (
    df.groupby("Location")["Salary_LPA"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
salary.plot(kind="bar")
plt.title("Average Salary by Location")
plt.xlabel("Location")
plt.ylabel("Average Salary (LPA)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/average_salary_by_location.png")
plt.close()


# --------------------------------
# 7. Salary Distribution
# --------------------------------

plt.figure(figsize=(8, 5))
df["Salary_LPA"].plot(
    kind="hist",
    bins=10
)
plt.title("Salary Distribution")
plt.xlabel("Salary (LPA)")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("output/salary_distribution.png")
plt.close()


print("=" * 50)
print("VISUALIZATION COMPLETED")
print("=" * 50)
print("All charts have been created successfully!")
print("Charts saved inside the output folder.")