
from fastapi import FastAPI
from pydantic import BaseModel
from agent import text_answer

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):

    answer, image = text_answer(query.question)

    return{
        "answer": answer,
        "image": image
    }
    

