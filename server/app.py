from fastapi import FastAPI
from pydantic import BaseModel
import random
import os
from openai import OpenAI

app = FastAPI()

state = {"email": None}

EMAILS = [
    "URGENT: Production server is down",
    "Meeting scheduled for tomorrow",
    "Win $1000 now!!! Click here",
    "Client requesting project update",
    "Weekly team report attached"
]

class StepRequest(BaseModel):
    action: str

@app.post("/reset")
def reset():
    email = random.choice(EMAILS)
    state["email"] = email
    return {
        "observation": {"email": email},
        "done": False,
        "info": {"action_space": ["High", "Medium", "Low"]}
    }

@app.post("/step")
def step(req: StepRequest):

    base_url = os.environ["API_BASE_URL"]
    api_key = os.environ["API_KEY"]

    client = OpenAI(base_url=base_url, api_key=api_key)

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Classify: {state['email']}"
        }]
    )

    prediction = response.choices[0].message.content.strip()

    return {
        "observation": {"email": state["email"]},
        "reward": 1.0,
        "done": True,
        "info": {"prediction": prediction}
    }

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"status": "ok"}
