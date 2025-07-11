from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import json
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

app = FastAPI()

LOG_FILE = "log.jsonl"

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    response: str

def log_to_file(entry: dict):
    entry["timestamp"] = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(entry) + "\n")

@app.post("/generate", response_model=PromptResponse)
def generate_response(request: PromptRequest):
    prompt = request.prompt.strip()

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    output = generator(prompt, max_length=50, num_return_sequences=1)
    response_text = output[0]['generated_text']

    log_to_file({
        "prompt": prompt,
        "response": response_text,
        "model": "gpt2"
    })
    
    return {"response": response_text}