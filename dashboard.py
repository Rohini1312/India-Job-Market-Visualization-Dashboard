import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------
# Page Configuration
# -----------------------------------------

st.set_page_config(
    page_title="India Job Market Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------------
# Load Data
# -----------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_job_market.csv")


df = load_data()

# -----------------------------------------
# Title
# -----------------------------------------

st.title("📊 India Job Market Visualization Dashboard")

st.markdown(
    "### Explore job opportunities, skills, experience levels and salary trends"
)

st.info(
    "Note: This project uses synthetic/demo data generated for educational purposes. "
    "It does not represent real-time India job-market statistics."
)

# -----------------------------------------
# Sidebar Filters
# -----------------------------------------

st.sidebar.header("🔎 Filters")

# Reset button
if st.sidebar.button("🔄 Reset Filters"):
    st.rerun()

# Location
locations = sorted(df["Location"].unique())

selected_locations = st.sidebar.multiselect(
    "📍 Select Location",
    locations,
    default=locations
)

# Company
companies = sorted(df["Company"].unique())

selected_companies = st.sidebar.multiselect(
    "🏢 Select Company",
    companies,
    default=companies
)

# Job Type
job_types = sorted(df["Job_Type"].unique())

selected_job_types = st.sidebar.multiselect(
    "💼 Select Job Type",
    job_types,
    default=job_types
)

# Experience
experiences = sorted(df["Experience"].unique())

selected_experiences = st.sidebar.multiselect(
    "🎓 Select Experience",
    experiences,
    default=experiences
)

# Skill
skills = sorted(df["Skill"].unique())

selected_skills = st.sidebar.multiselect(
    "💻 Select Skill",
    skills,
    default=skills
)

# Job Title
job_titles = sorted(df["Job_Title"].unique())

selected_job_titles = st.sidebar.multiselect(
    "🧑‍💻 Select Job Title",
    job_titles,
    default=job_titles
)

# Salary Range
min_salary = int(df["Salary_LPA"].min())
max_salary = int(df["Salary_LPA"].max())

salary_range = st.sidebar.slider(
    "💰 Salary Range (LPA)",
    min_value=min_salary,
    max_value=max_salary,
    value=(min_salary, max_salary)
)

# -----------------------------------------
# Apply Filters
# -----------------------------------------

filtered_df = df[
    df["Location"].isin(selected_locations)
    & df["Company"].isin(selected_companies)
    & df["Job_Type"].isin(selected_job_types)
    & df["Experience"].isin(selected_experiences)
    & df["Skill"].isin(selected_skills)
    & df["Job_Title"].isin(selected_job_titles)
    & df["Salary_LPA"].between(
        salary_range[0],
        salary_range[1]
    )
]

# -----------------------------------------
# Filter Summary
# -----------------------------------------

st.sidebar.markdown("---")

st.sidebar.write(
    f"**Filtered Jobs:** {len(filtered_df)}"
)

st.sidebar.write(
    f"**Salary:** {salary_range[0]} - {salary_range[1]} LPA"
)

# -----------------------------------------
# KPI Section
# -----------------------------------------

st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Jobs",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Companies",
        filtered_df["Company"].nunique()
    )

with col3:
    st.metric(
        "Locations",
        filtered_df["Location"].nunique()
    )

with col4:
    if len(filtered_df) > 0:
        avg_salary = filtered_df["Salary_LPA"].mean()

        st.metric(
            "Average Salary",
            f"{avg_salary:.2f} LPA"
        )
    else:
        st.metric(
            "Average Salary",
            "0 LPA"
        )

# -----------------------------------------
# Empty Filter Result
# -----------------------------------------

if filtered_df.empty:

    st.warning(
        "⚠️ No jobs match the selected filters. "
        "Please change the filters."
    )

else:

    # -------------------------------------
    # Jobs by Location
    # -------------------------------------

    st.subheader("📍 Jobs by Location")

    location_data = (
        filtered_df["Location"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    location_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Location")
    ax.set_ylabel("Number of Jobs")
    ax.set_title("Jobs by Location")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # -------------------------------------
    # Jobs by Company
    # -------------------------------------

    st.subheader("🏢 Jobs by Company")

    company_data = (
        filtered_df["Company"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    company_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Company")
    ax.set_ylabel("Number of Jobs")
    ax.set_title("Jobs by Company")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # -------------------------------------
    # Jobs by Skill
    # -------------------------------------

    st.subheader("💻 Most Demanded Skills")

    skill_data = (
        filtered_df["Skill"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    skill_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Skill")
    ax.set_ylabel("Number of Jobs")
    ax.set_title("Most Demanded Skills")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # -------------------------------------
    # Jobs by Job Title
    # -------------------------------------

    st.subheader("🧑‍💻 Jobs by Job Title")

    title_data = (
        filtered_df["Job_Title"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    title_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Job Title")
    ax.set_ylabel("Number of Jobs")
    ax.set_title("Jobs by Job Title")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # -------------------------------------
    # Jobs by Experience
    # -------------------------------------

    st.subheader("🎓 Jobs by Experience Level")

    experience_data = (
        filtered_df["Experience"]
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    experience_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Experience")
    ax.set_ylabel("Number of Jobs")
    ax.set_title("Jobs by Experience Level")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # -------------------------------------
    # Job Type Distribution
    # -------------------------------------

    st.subheader("💼 Job Type Distribution")

    job_type_data = (
        filtered_df["Job_Type"]
        .value_counts()
    )

    fig, ax = plt.subplots(figsize=(7, 5))

    job_type_data.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax
    )

    ax.set_ylabel("")
    ax.set_title("Job Type Distribution")

    st.pyplot(fig)

    # -------------------------------------
    # Average Salary by Location
    # -------------------------------------

    st.subheader("💰 Average Salary by Location")

    salary_data = (
        filtered_df
        .groupby("Location")["Salary_LPA"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    salary_data.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Location")
    ax.set_ylabel("Average Salary (LPA)")
    ax.set_title("Average Salary by Location")

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # -------------------------------------
    # Salary Distribution
    # -------------------------------------

    st.subheader("💵 Salary Distribution")

    fig, ax = plt.subplots(figsize=(10, 5))

    filtered_df["Salary_LPA"].plot(
        kind="hist",
        bins=10,
        ax=ax
    )

    ax.set_xlabel("Salary (LPA)")
    ax.set_ylabel("Number of Jobs")
    ax.set_title("Salary Distribution")

    plt.tight_layout()

    st.pyplot(fig)

    # -------------------------------------
    # Highest Salary
    # -------------------------------------

    st.subheader("🏆 Salary Summary")

    salary_col1, salary_col2, salary_col3 = st.columns(3)

    with salary_col1:
        st.metric(
            "Lowest Salary",
            f"{filtered_df['Salary_LPA'].min()} LPA"
        )

    with salary_col2:
        st.metric(
            "Average Salary",
            f"{filtered_df['Salary_LPA'].mean():.2f} LPA"
        )

    with salary_col3:
        st.metric(
            "Highest Salary",
            f"{filtered_df['Salary_LPA'].max()} LPA"
        )

    # -------------------------------------
    # Job Data Table
    # -------------------------------------

    st.subheader("📋 Job Market Data")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # -------------------------------------
    # Download Filtered Data
    # -------------------------------------

    st.subheader("📥 Download Data")

    csv_data = filtered_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Filtered Data",
        data=csv_data,
        file_name="filtered_job_market.csv",
        mime="text/csv"
    )

# -----------------------------------------
# Footer
# -----------------------------------------

st.markdown("---")

st.caption(
    "India Job Market Visualization Dashboard | "
    "Python + Pandas + Matplotlib + Streamlit"
)