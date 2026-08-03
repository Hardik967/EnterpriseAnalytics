from sqlalchemy.orm import Session
from sqlalchemy import func

from models import Job, Salary, Company, JobSkill


# ------------------------------
# Jobs by Location
# ------------------------------
def jobs_by_location(db: Session):

    result = (
        db.query(
            Job.location,
            func.count(Job.job_id).label("jobs")
        )
        .group_by(Job.location)
        .order_by(func.count(Job.job_id).desc())
        .limit(10)
        .all()
    )

    return [
        {
            "location": row.location,
            "jobs": row.jobs
        }
        for row in result
    ]


# ------------------------------
# Work Type Distribution
# ------------------------------
def work_type_distribution(db: Session):

    result = (
        db.query(
            Job.work_type,
            func.count(Job.job_id).label("count")
        )
        .group_by(Job.work_type)
        .all()
    )

    return [
        {
            "work_type": row.work_type,
            "count": row.count
        }
        for row in result
    ]


# ------------------------------
# Salary Distribution
# ------------------------------
def salary_distribution(db: Session):

    result = (
        db.query(
            Salary.pay_period,
            func.avg(Salary.max_salary).label("avg_salary")
        )
        .group_by(Salary.pay_period)
        .all()
    )

    return [
        {
            "pay_period": row.pay_period,
            "average_salary": round(row.avg_salary or 0, 2)
        }
        for row in result
    ]


# ------------------------------
# Top Hiring Companies
# ------------------------------
def top_hiring_companies(db: Session):

    result = (
        db.query(
            Company.name,
            func.count(Job.job_id).label("jobs")
        )
        .join(Job, Company.company_id == Job.company_id)
        .group_by(Company.company_id)
        .order_by(func.count(Job.job_id).desc())
        .limit(10)
        .all()
    )

    return [
        {
            "company": row.name,
            "jobs": row.jobs
        }
        for row in result
    ]


# ------------------------------
# Top Skills
# ------------------------------
def top_skills(db: Session):

    result = (
        db.query(
            JobSkill.skill_abr,
            func.count(JobSkill.job_id).label("count")
        )
        .group_by(JobSkill.skill_abr)
        .order_by(func.count(JobSkill.job_id).desc())
        .limit(10)
        .all()
    )

    return [
        {
            "skill": row.skill_abr,
            "jobs": row.count
        }
        for row in result
    ]