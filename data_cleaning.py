import pandas as pd

input_file = "data/india_job_market.csv"
output_file = "data/cleaned_job_market.csv"

# Load dataset
df = pd.read_csv(input_file)

print("=" * 50)
print("DATA CLEANING")
print("=" * 50)

print("Original rows:", len(df))

# Remove duplicate records
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Remove invalid salary values
df = df[df["Salary_LPA"] > 0]

# Remove invalid job records
df = df[df["Job_Title"].str.strip() != ""]
df = df[df["Company"].str.strip() != ""]
df = df[df["Location"].str.strip() != ""]

# Save cleaned dataset
df.to_csv(output_file, index=False)

print("Cleaning completed successfully!")
print("Cleaned rows:", len(df))
print("Saved to:", output_file)