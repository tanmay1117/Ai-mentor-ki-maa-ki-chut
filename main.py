from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuizInput(BaseModel):
    answers: list[str]

@app.post("/infer")
async def infer_career(input: QuizInput):
    # Placeholder: Replace with NLP logic
    return {"career": "Backend Developer", "resources": []}
