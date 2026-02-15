import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
from schemas import AnalyzeRequest, AnalyzeResponse
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE

load_dotenv()

app = FastAPI(title="RealitySplit API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
else:
    model = None


@app.get("/")
async def root():
    return {"message": "RealitySplit API is running"}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_article(request: AnalyzeRequest):
    if not model:
        raise HTTPException(status_code=500, detail="Gemini API key not configured")

    try:
        prompt = USER_PROMPT_TEMPLATE.format(article=request.article)

        response = model.generate_content(
            f"{SYSTEM_PROMPT}\n\n{prompt}",
            generation_config={"response_mime_type": "application/json"},
        )

        data = json.loads(response.text)

        # Handle cases where LLM might return a list of one object
        if isinstance(data, list) and len(data) > 0:
            data = data[0]

        if not isinstance(data, dict):
            raise ValueError(f"Expected dictionary response, got {type(data)}")

        # Ensure 'original' is included in data if LLM didn't return it
        if "original" not in data:
            data["original"] = request.article

        return data
    except Exception as e:
        import traceback

        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
