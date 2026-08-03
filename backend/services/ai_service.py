import os
from dotenv import load_dotenv
from google import genai
from sqlalchemy import func

from database import SessionLocal
from models import Job, Company, Salary, Skill

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_insights(question: str):

    db = SessionLocal()

    total_jobs = db.query(Job).count()

    total_companies = db.query(Company).count()

    avg_salary = (
        db.query(func.avg(Salary.max_salary))
        .scalar()
    )

    top_locations = (
        db.query(
            Job.location,
            func.count(Job.job_id)
        )
        .group_by(Job.location)
        .order_by(func.count(Job.job_id).desc())
        .limit(5)
        .all()
    )

    top_work_types = (
        db.query(
            Job.work_type,
            func.count(Job.job_id)
        )
        .group_by(Job.work_type)
        .order_by(func.count(Job.job_id).desc())
        .all()
    )

    total_skills = db.query(Skill).count()

    db.close()

    prompt = f"""
You are TalentIQ AI.

Below is recruitment data from my database.

Total Jobs: {total_jobs}

Total Companies: {total_companies}

Average Salary: {avg_salary:.2f}

Total Skills: {total_skills}

Top Hiring Locations:
{top_locations}

Work Types:
{top_work_types}

Answer the user's question using this database first.

If the database does not contain enough information,
then use your general knowledge.

Question:

{question}
"""

    response = client.models.generate_content(
        model="models/gemini-3.5-flash",
        contents=prompt
    )

    return response.text