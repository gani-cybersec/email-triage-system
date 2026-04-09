import json
import os


def load_data():
    """
    Safe data loader (hackathon compliant)
    Always returns a valid list.
    """

    try:
        base_dir = os.path.dirname(__file__)
        path = os.path.join(base_dir, "data", "emails.json")

        # -------------------------------
        # FILE EXISTS CHECK
        # -------------------------------
        if not os.path.exists(path):
            return [
                {"text": "Fallback email: server running.", "label": "Low"}
            ]

        # -------------------------------
        # LOAD JSON
        # -------------------------------
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # -------------------------------
        # VALIDATE FORMAT
        # -------------------------------
        if not isinstance(data, list) or len(data) == 0:
            return [
                {"text": "Fallback email: invalid dataset.", "label": "Low"}
            ]

        # -------------------------------
        # NORMALIZE DATA
        # -------------------------------
        safe_data = []
        for email in data:
            text = (
                email.get("text")
                or email.get("input")
                or email.get("message")
                or ""
            )

            label = email.get("label", "Low")

            safe_data.append({
                "text": text,
                "label": label
            })

        return safe_data

    except Exception:
        # -------------------------------
        # FAIL SAFE (VERY IMPORTANT)
        # -------------------------------
        return [
            {"text": "Fallback email: error loading data.", "label": "Low"}
        ]
