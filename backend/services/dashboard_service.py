from sqlalchemy.orm import Session
from sqlalchemy import func

from models import Company, Job, Salary, Skill


def get_dashboard(db: Session):

    total_jobs = db.query(func.count(Job.job_id)).scalar()

    total_companies = db.query(func.count(Company.company_id)).scalar()

    total_skills = db.query(func.count(Skill.skill_abr)).scalar()

    average_salary = db.query(func.avg(Salary.max_salary)).scalar()

    return {
        "total_jobs": total_jobs,
        "total_companies": total_companies,
        "total_skills": total_skills,
        "average_salary": round(average_salary or 0, 2)
    }