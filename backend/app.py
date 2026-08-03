from fastapi import FastAPI

from database import engine
from models import Base

from api.dashboard import router as dashboard_router
from api.jobs import router as jobs_router
from api.companies import router as company_router
from api.analytics import router as analytics_router
from api.ai import router as ai_router
from api.dashboard_charts import router as chart_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(dashboard_router)
app.include_router(jobs_router)
app.include_router(company_router)
app.include_router(analytics_router)
app.include_router(ai_router)
app.include_router(chart_router)


@app.get("/")
def home():
    return {"message": "TalentIQ API Running"}