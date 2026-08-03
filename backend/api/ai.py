from fastapi import APIRouter
from pydantic import BaseModel

from services.ai_service import generate_insights

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

class AIRequest(BaseModel):
    question: str


@router.post("/insights")
def ai(request: AIRequest):

    answer = generate_insights(request.question)

    return {
        "answer": answer
    }