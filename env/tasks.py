import random
from .data_loader import load_data


# -------------------------------
# SAFE RANDOM EMAIL FETCHER
# -------------------------------
def get_random_email():
    try:
        emails = load_data()

        # -------------------------------
        # SAFETY: If dataset is empty
        # -------------------------------
        if not emails or len(emails) == 0:
            return {
                "text": "Test email: server is running normally.",
                "label": "Low"
            }

        # -------------------------------
        # PICK RANDOM EMAIL
        # -------------------------------
        email = random.choice(emails)

        # -------------------------------
        # NORMALIZE KEYS (VERY IMPORTANT)
        # -------------------------------
        text = (
            email.get("text")
            or email.get("input")
            or email.get("message")
            or ""
        )

        label = email.get("label", "Low")

        # -------------------------------
        # FINAL SAFE OUTPUT
        # -------------------------------
        return {
            "text": text,
            "label": label
        }

    except Exception:
        # -------------------------------
        # FAIL-SAFE (MANDATORY)
        # -------------------------------
        return {
            "text": "Fallback email: unable to load dataset.",
            "label": "Low"
        }
