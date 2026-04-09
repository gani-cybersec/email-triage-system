import os
from openai import OpenAI
from utils import clean_text

# -------------------------------
# INIT CLIENT
# -------------------------------
client = OpenAI(
    api_key=os.environ.get("HF_TOKEN"),
    base_url=os.environ.get("API_BASE_URL")
)

MODEL = os.environ.get("MODEL_NAME", "gpt-4o-mini")


# -------------------------------
# SAFE RESPONSE PARSER
# -------------------------------
def safe_extract(text, allowed):
    text = text.strip().lower()

    for option in allowed:
        if option.lower() in text:
            return option

    return allowed[0]  # fallback


# -------------------------------
# PRIORITY CLASSIFICATION
# -------------------------------
def choose_action(email):
    email = clean_text(email)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{
                "role": "user",
                "content": f"""
Classify the priority of this email.

Return ONLY one word:
High OR Medium OR Low

Email:
{email}
"""
            }],
            temperature=0
        )

        output = response.choices[0].message.content
        return safe_extract(output, ["High", "Medium", "Low"])

    except Exception:
        return "Low"   # safe fallback


# -------------------------------
# SPAM DETECTION
# -------------------------------
def detect_spam(email):
    email = clean_text(email)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{
                "role": "user",
                "content": f"""
Is this email spam?

Return ONLY:
Spam OR Not Spam

Email:
{email}
"""
            }],
            temperature=0
        )

        output = response.choices[0].message.content
        return safe_extract(output, ["Spam", "Not Spam"])

    except Exception:
        return "Not Spam"


# -------------------------------
# AUTO REPLY
# -------------------------------
def generate_reply(email, priority, spam_status):
    email = clean_text(email)

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{
                "role": "user",
                "content": f"""
Generate a short professional email reply.

Priority: {priority}
Spam Status: {spam_status}

Keep it concise and relevant.

Email:
{email}
"""
            }],
            temperature=0.5
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return "Thank you for your email. We will get back to you soon."


# -------------------------------
# LEARNING HOOK (OPTIONAL)
# -------------------------------
def learn(email, action, reward):
    """
    Optional reinforcement learning hook.
    Currently unused but kept for extensibility.
    """
    return {
        "status": "logged",
        "action": action,
        "reward": reward
    }
