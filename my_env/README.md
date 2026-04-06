# 📧 OpenMail RL - Adaptive Email Triage System

## 🚀 Overview
OpenMail RL is a Reinforcement Learning-based email triage system that learns to prioritize emails dynamically using feedback.

Instead of using fixed rules, the system improves over time by learning from rewards, following OpenEnv principles.

---

## 🧠 Key Idea

We model email prioritization as an RL problem:

- **Observation** → Email text  
- **Action** → Priority (High / Medium / Low)  
- **Reward** → +1 (correct), -1 (incorrect)

The agent learns to make better decisions over time.

---

## ✨ Features

- 📧 Email classification (High / Medium / Low)
- 🔁 Reinforcement Learning loop (learn from feedback)
- 🌐 FastAPI-based environment (OpenEnv style)
- 🤖 Adaptive agent with memory-based learning
- 🐳 Docker support for deployment

---

## 🏗️ Project Structure
