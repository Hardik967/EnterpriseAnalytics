from fastapi import APIRouter
from database import SessionLocal

from services.analytics_service import *

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/jobs-by-location")
def location():

    db = SessionLocal()

    try:
        return jobs_by_location(db)
    finally:
        db.close()


@router.get("/work-type")
def worktype():

    db = SessionLocal()

    try:
        return work_type_distribution(db)
    finally:
        db.close()


@router.get("/salary")
def salary():

    db = SessionLocal()

    try:
        return salary_distribution(db)
    finally:
        db.close()


@router.get("/top-companies")
def companies():

    db = SessionLocal()

    try:
        return top_hiring_companies(db)
    finally:
        db.close()


@router.get("/top-skills")
def skills():

    db = SessionLocal()

    try:
        return top_skills(db)
    finally:
        db.close()