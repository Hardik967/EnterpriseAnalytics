from fastapi import APIRouter
from sqlalchemy import func

from database import SessionLocal
from models import Job, Salary

router = APIRouter(
    prefix="/charts",
    tags=["Charts"]
)

@router.get("/work-types")
def work_types():

    db = SessionLocal()

    data = (
        db.query(
            Job.work_type,
            func.count(Job.job_id)
        )
        .group_by(Job.work_type)
        .all()
    )

    db.close()

    return [
        {
            "work_type": i[0],
            "count": i[1]
        }
        for i in data
    ]


@router.get("/salary-distribution")
def salary_distribution():

    db = SessionLocal()

    data = db.query(Salary.max_salary).all()

    db.close()

    return [
        i[0]
        for i in data
        if i[0]
    ]