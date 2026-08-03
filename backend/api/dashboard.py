from fastapi import APIRouter
from database import SessionLocal

from services.dashboard_service import get_dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard():

    db = SessionLocal()

    try:
        return get_dashboard(db)

    finally:
        db.close()