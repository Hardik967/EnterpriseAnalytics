from sqlalchemy.orm import Session
from models import Job


def get_all_jobs(db: Session):
    jobs = db.query(Job).limit(100).all()

    result = []

    for job in jobs:
        result.append({
            "job_id": job.job_id,
            "company_id": job.company_id,
            "title": job.title,
            "location": job.location,
            "work_type": job.work_type,
            "views": job.views
        })

    return result


def get_job_by_id(db: Session, job_id: int):

    job = db.query(Job).filter(Job.job_id == job_id).first()

    if not job:
        return {"message": "Job not found"}

    return {
        "job_id": job.job_id,
        "company_id": job.company_id,
        "title": job.title,
        "description": job.description,
        "location": job.location,
        "work_type": job.work_type,
        "views": job.views
    }


def search_jobs(db: Session, keyword: str):

    jobs = db.query(Job).filter(
        Job.title.ilike(f"%{keyword}%")
    ).limit(50).all()

    result = []

    for job in jobs:
        result.append({
            "job_id": job.job_id,
            "title": job.title,
            "location": job.location,
            "work_type": job.work_type
        })

    return result