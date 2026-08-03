import pandas as pd
from database import SessionLocal
from models import Company, Job, Salary, Skill, JobSkill

session = SessionLocal()


def safe_value(value):
    if pd.isna(value):
        return None
    return value


# -----------------------------
# Clear Existing Data
# -----------------------------
print("Clearing existing data...")

session.query(JobSkill).delete()
session.query(Salary).delete()
session.query(Skill).delete()
session.query(Job).delete()
session.query(Company).delete()

session.commit()


# -----------------------------
# Companies
# -----------------------------
print("Loading companies...")

companies = pd.read_csv("../data/companies.csv")

for _, row in companies.iterrows():

    company = Company(
        company_id=safe_value(row["company_id"]),
        name=safe_value(row["name"]),
        description=safe_value(row["description"])
    )

    session.add(company)

session.commit()

print(f"Imported {len(companies)} companies")


# -----------------------------
# Jobs
# -----------------------------
print("Loading jobs...")

jobs = pd.read_csv("../data/postings.csv")

for _, row in jobs.iterrows():

    job = Job(
        job_id=safe_value(row["job_id"]),
        company_id=safe_value(row["company_id"]),
        title=safe_value(row["title"]),
        description=safe_value(row["description"]),
        location=safe_value(row["location"]),
        work_type=safe_value(row["formatted_work_type"]),
        views=safe_value(row["views"])
    )

    session.add(job)

session.commit()

print(f"Imported {len(jobs)} jobs")


# -----------------------------
# Salaries
# -----------------------------
print("Loading salaries...")

salary_df = pd.read_csv("../data/salaries.csv")

for _, row in salary_df.iterrows():

    salary = Salary(
        job_id=safe_value(row["job_id"]),
        max_salary=safe_value(row["max_salary"]),
        pay_period=safe_value(row["pay_period"])
    )

    session.add(salary)

session.commit()

print(f"Imported {len(salary_df)} salary records")


# -----------------------------
# Skills
# -----------------------------
print("Loading skills...")

skills = pd.read_csv("../data/skills.csv")

for _, row in skills.iterrows():

    skill = Skill(
        skill_abr=safe_value(row["skill_abr"]),
        skill_name=safe_value(row["skill_name"])
    )

    session.add(skill)

session.commit()

print(f"Imported {len(skills)} skills")


# -----------------------------
# Job Skills
# -----------------------------
print("Loading job skills...")

job_skills = pd.read_csv("../data/job_skills.csv")

for _, row in job_skills.iterrows():

    job_skill = JobSkill(
        job_id=safe_value(row["job_id"]),
        skill_abr=safe_value(row["skill_abr"])
    )

    session.add(job_skill)

session.commit()

print(f"Imported {len(job_skills)} job skills")


session.close()

print("\n===================================")
print("Database imported successfully!")
print("===================================")