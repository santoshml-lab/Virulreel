from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GROQ
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# REQUEST MODEL
class ReelRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"status":"ViralReel AI running 🚀"}

# 🎣 HOOK GENERATOR
@app.post("/generate-hook")
def hook(data: ReelRequest):

    prompt = f"""
Generate 5 viral Instagram reel hooks for:

Topic: {data.topic}

Rules:
- short
- catchy
- Gen Z style
- emotional or shocking
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role":"system",
            "content":prompt
        }],
        max_tokens=400
    )

    return {
        "hooks": response.choices[0].message.content
    }

# 🎬 SCRIPT GENERATOR
@app.post("/generate-script")
def script(data: ReelRequest):

    prompt = f"""
Generate a short viral reel script.

Topic: {data.topic}

Format:
- Hook
- Main content
- Ending CTA

Style:
- engaging
- viral
- creator style
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role":"system",
            "content":prompt
        }],
        max_tokens=700
    )

    return {
        "script": response.choices[0].message.content
    }

# ✍ CAPTION GENERATOR
@app.post("/generate-caption")
def caption(data: ReelRequest):

    prompt = f"""
Generate Instagram captions for:

Topic: {data.topic}

Rules:
- short
- emotional
- engaging
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role":"system",
            "content":prompt
        }],
        max_tokens=300
    )

    return {
        "caption": response.choices[0].message.content
    }

# 🔥 HASHTAG GENERATOR
@app.post("/generate-hashtags")
def hashtags(data: ReelRequest):

    prompt = f"""
Generate viral hashtags for:

Topic: {data.topic}

Give only hashtags.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{
            "role":"system",
            "content":prompt
        }],
        max_tokens=200
    )

    return {
        "hashtags": response.choices[0].message.content
    }
