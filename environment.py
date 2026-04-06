from .tasks import get_random_email
from .graders import compute_reward


class EmailTriageEnv:
    def __init__(self):
        self.current_email = None
        self.done = False

    def reset(self):
        self.current_email = get_random_email()
        self.done = False

        return {
            "email": self.current_email["text"]
        }

    def detect_spam(self, email):
        email = email.lower()

        spam_keywords = [
            "bank details",
            "verify account",
            "account blocked",
            "urgent action",
            "click here",
            "limited time",
            "lottery",
            "win money",
            "free offer",
            "send your details",
            "password",
            "credit card"
        ]

        for keyword in spam_keywords:
            if keyword in email:
                return "Spam"

        return "Not Spam"

    def generate_reply(self, priority):
        if priority == "High":
            return "Thank you for your urgent email. We are addressing your issue immediately."
        elif priority == "Medium":
            return "Thank you for reaching out. We will get back to you shortly."
        else:
            return "Thank you for your message. We appreciate your feedback."

    def step(self, action):
        if self.current_email is None:
            return {
                "error": "Call /reset before /step"
            }

        email_text = self.current_email["text"]
        correct = self.current_email["label"]

        # RL reward
        reward = compute_reward(action, correct)

        # NEW FEATURES
        spam_status = self.detect_spam(email_text)
        auto_reply = self.generate_reply(action)

        self.done = True

        return {
            "observation": email_text,
            "predicted_priority": action,
            "spam_status": spam_status,
            "auto_reply": auto_reply,
            "reward": reward,
            "done": self.done,
            "correct_label": correct,
            "info": {
                "message": "Step completed"
            }
        }