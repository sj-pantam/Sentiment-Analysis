import ollama
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/analyze")
def analyze(text: str = Form(...)):
    prompt = f"What is the sentiment of this text? Respond with Positive, Negative, or Neutral:\n\n{text}"
    
    response = ollama.generate(
        model="mistral",
        prompt=prompt,
        stream=False 
    )
    
    return {"sentiment": response["response"].strip()}