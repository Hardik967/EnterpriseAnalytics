from fastapi import APIRouter
from database import SessionLocal

from services.company_service import *

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


@router.get("/")
def companies():

    db = SessionLocal()

    try:
        return get_all_companies(db)

    finally:
        db.close()


@router.get("/top-hiring")
def top():

    db = SessionLocal()

    try:
        return top_hiring_companies(db)

    finally:
        db.close()


@router.get("/{company_id}")
def company(company_id: int):

    db = SessionLocal()

    try:
        return get_company(db, company_id)

    finally:
        db.close()