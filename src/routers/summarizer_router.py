from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from openai import OpenAI

router = APIRouter(prefix="/api/summarize", tags=["summarizer"])

class TextRequest(BaseModel):
    text: str

@router.post("/")
async def summarize_text(request: TextRequest):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Du bist ein Textzusammenfasser. Fasse den Text klar und präzise zusammen."},
                {"role": "user", "content": request.text},
            ],
            temperature=0.5,
        )

        summary = response.choices[0].message.content
        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
