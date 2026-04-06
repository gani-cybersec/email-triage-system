# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Expose Streamlit port
EXPOSE 7860

# ✅ Run BOTH FastAPI + Streamlit
CMD ["bash", "-c", "uvicorn server:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 7860 --server.address 0.0.0.0"]