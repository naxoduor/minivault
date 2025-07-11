# 🧠 Minivault (FastAPI + Transformers)

This project is a lightweight REST API built with FastAPI and Hugging Face Transformers that:

- Accepts a text prompt via POST request
- Returns a generated response (default model: `gpt2`)
- Logs both request and response to a local `log.jsonl` file

Runs entirely locally and containerized with Docker.

---

## 📦 Requirements

- Docker
- Internet connection (on first build to download the model)

---

## 🚀 Quick Start

### Steps to Run the App using Docker

```bash
git clone https://github.com/naxoduor/minivault.git
cd minivault

docker build -t minivault .


docker run -p 8000:8000 minivault

---
### Test the app
curl -X POST http://localhost:8000/generate   -H "Content-Type: application/json"   -d '{"prompt": "What is AI"}'

----
## Sample response

A few years ago, when the brain was a little more mature, we discussed the concept of AI, the concept of a \"real world.\" Now, the brain has come a long way and we have all the information we need to build a fully functional, self-driving car.\n\nWhat is the future of the brain?\n\nThe future is the future of technology. The future is not just about AI. It is also about how the brains work, how they work, and how they're connected to the rest of the brain. If the brain works, the brain will work. If the brain doesn't work, the brain will work.\n\nIs there a market for AI?\n\nYes, there is. The market for AI is a very complicated one. It's a lot of work, a lot of work. But there are some companies that are making great ideas for AI, and they're doing it well.\n\nWhat is your vision for AI?\n\nIf you have the money to pay for AI, that's what you're going to do.\n\nWhat is the future of technology?\n\nI don't have a strong vision, but I think we're going to find a way to make technology a"}
