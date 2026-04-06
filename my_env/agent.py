import random
from utils import clean_text

ACTIONS = ["High", "Medium", "Low"]

# memory (stores learned actions)
memory = {}

# -------------------------------
# ACTION SELECTION (SMART)
# -------------------------------
def choose_action(email):
    email = clean_text(email)

    # if already learned, return stored action
    if email in memory:
        return memory[email]

    # 🔥 HIGH priority keywords
    if any(word in email for word in [
        "urgent", "immediately", "asap", "down", "error", "failed", "issue", "critical"
    ]):
        return "High"

    # 🔥 MEDIUM priority keywords
    elif any(word in email for word in [
        "meeting", "schedule", "update", "request", "follow up", "review"
    ]):
        return "Medium"

    # 🔥 LOW priority keywords
    elif any(word in email for word in [
        "newsletter", "promotion", "sale", "offer", "discount"
    ]):
        return "Low"

    # fallback
    return "Medium"


# -------------------------------
# LEARNING FUNCTION
# -------------------------------
def learn(email, action, reward):
    email = clean_text(email)

    if reward == 1:
        memory[email] = action


# -------------------------------
# SPAM DETECTION
# -------------------------------
def detect_spam(email):
    spam_keywords = [
        "win", "free", "offer", "click", "buy now",
        "discount", "prize", "limited time"
    ]

    email = clean_text(email)

    for word in spam_keywords:
        if word in email:
            return "Spam"

    return "Not Spam"


# -------------------------------
# AUTO REPLY
# -------------------------------
def generate_reply(email, priority, spam_status):
    email = clean_text(email)

    if spam_status == "Spam":
        return "This email is identified as spam. No reply is sent."

    if priority == "High":
        return "Thank you for your urgent email. We are addressing your issue immediately."

    elif priority == "Medium":
        return "Thank you for your email. We will respond shortly."

    else:
        return "Thank you for reaching out. We will review your message soon."
