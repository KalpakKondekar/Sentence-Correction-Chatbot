from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class ChatRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Backend Running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Correct the grammar and spelling of the sentence."
            },
            {
                "role": "user",
                "content": request.text
            }
        ],
        temperature=0.2
    )

    corrected_text = response.choices[0].message.content

    return {
        "original": request.text,
        "corrected": corrected_text
    }