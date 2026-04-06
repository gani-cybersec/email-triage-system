from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import EmailTriageEnv
from agent import choose_action, detect_spam, generate_reply

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="OpenMail RL API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize environment
env = EmailTriageEnv()


# -------------------------------
# Request Models
# -------------------------------

class ActionRequest(BaseModel):
    action: str

class EmailRequest(BaseModel):
    email: str


# -------------------------------
# ROOT
# -------------------------------

@app.get("/")
def home():
    return {
        "message": "Email Triage RL Server Running 🚀",
        "endpoints": ["/reset", "/step", "/predict"]
    }


# -------------------------------
# TRAINING MODE
# -------------------------------

@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(request: ActionRequest):
    try:
        result = env.step(request.action)
        return result
    except Exception as e:
        return {"error": str(e)}


# -------------------------------
# PREDICTION MODE
# -------------------------------

@app.post("/predict")
def predict(request: EmailRequest):
    try:
        # Priority
        priority = choose_action(request.email)

        # Spam detection
        spam_status = detect_spam(request.email)

        # 🔥 Auto reply
        reply = generate_reply(request.email, priority, spam_status)

        return {
            "email": request.email,
            "predicted_priority": priority,
            "spam_status": spam_status,
            "auto_reply": reply
        }

    except Exception as e:
        return {"error": str(e)}
