from fastapi import APIRouter
from database import SessionLocal

from services.job_service import (
    get_all_jobs,
    get_job_by_id,
    search_jobs
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/")
def all_jobs():

    db = SessionLocal()

    try:
        return get_all_jobs(db)

    finally:
        db.close()


@router.get("/{job_id}")
def job(job_id: int):

    db = SessionLocal()

    try:
        return get_job_by_id(db, job_id)

    finally:
        db.close()


@router.get("/search/{keyword}")
def search(keyword: str):

    db = SessionLocal()

    try:
        return search_jobs(db, keyword)

    finally:
        db.close()