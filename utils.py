import re


def clean_text(text):
    """
    Clean and normalize email text for LLM processing.
    """

    # -------------------------------
    # TYPE SAFETY
    # -------------------------------
    if text is None:
        return ""

    text = str(text)

    # -------------------------------
    # LOWERCASE
    # -------------------------------
    text = text.lower()

    # -------------------------------
    # REMOVE URLS
    # -------------------------------
    text = re.sub(r"http\S+|www\S+", "", text)

    # -------------------------------
    # REMOVE SPECIAL CHARACTERS
    # (keep letters + basic punctuation)
    # -------------------------------
    text = re.sub(r"[^a-z\s\.\,\!\?]", "", text)

    # -------------------------------
    # REMOVE EXTRA SPACES
    # -------------------------------
    text = re.sub(r"\s+", " ", text).strip()

    # -------------------------------
    # LIMIT LENGTH (IMPORTANT ⚠️)
    # -------------------------------
    max_length = 500
    if len(text) > max_length:
        text = text[:max_length]

    return text
