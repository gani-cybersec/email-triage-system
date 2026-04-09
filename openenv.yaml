version: "1"

services:
  app:
    build: .
    command: python -m server.app
    ports:
      - "7860:7860"

evaluation:
  inference_script: inference.py

env:
  API_BASE_URL: ${API_BASE_URL}
  API_KEY: ${API_KEY}
