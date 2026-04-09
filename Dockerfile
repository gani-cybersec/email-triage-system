# -------------------------------
# BASE IMAGE
# -------------------------------
FROM python:3.10-slim

# -------------------------------
# ENV SETTINGS
# -------------------------------
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# -------------------------------
# WORKDIR
# -------------------------------
WORKDIR /app

# -------------------------------
# INSTALL DEPENDENCIES
# -------------------------------
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# -------------------------------
# COPY PROJECT FILES
# -------------------------------
COPY . .

# -------------------------------
# EXPOSE PORT (FIXED ✅)
# -------------------------------
EXPOSE 7860

# -------------------------------
# RUN SERVER (FIXED ✅)
# -------------------------------
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]
