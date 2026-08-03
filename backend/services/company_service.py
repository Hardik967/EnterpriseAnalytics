from sqlalchemy.orm import Session
from sqlalchemy import func

from models import Company, Job


def get_all_companies(db: Session):

    companies = db.query(Company).limit(100).all()

    data = []

    for company in companies:

        data.append({
            "company_id": company.company_id,
            "name": company.name,
            "description": company.description
        })

    return data


def get_company(db: Session, company_id: int):

    company = db.query(Company).filter(
        Company.company_id == company_id
    ).first()

    if not company:
        return {"message": "Company not found"}

    total_jobs = db.query(func.count(Job.job_id)).filter(
        Job.company_id == company_id
    ).scalar()

    return {
        "company_id": company.company_id,
        "name": company.name,
        "description": company.description,
        "total_jobs": total_jobs
    }


def top_hiring_companies(db: Session):

    companies = (
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

    result = []

    for company in companies:

        result.append({
            "company": company.name,
            "jobs": company.jobs
        })

    return result