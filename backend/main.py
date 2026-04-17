from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# -------------------------
# INPUT MODEL
# -------------------------
class CodeInput(BaseModel):
    code: str


# -------------------------
# MAIN ENDPOINT
# -------------------------
@app.post("/generate-tests")
def generate_tests(data: CodeInput):

    # -------------------------
    # STRICT PROMPT (CRITICAL FIX)
    # -------------------------
    prompt = f"""
You are a senior QA engineer writing production-ready Jest test cases.

STRICT RULES:
- Output ONLY valid JavaScript test code
- DO NOT include explanations
- DO NOT include comments
- DO NOT include markdown (no ``` blocks)
- DO NOT include installation instructions
- DO NOT include text before or after code
- DO NOT include pseudo code or placeholders
- MUST use valid Jest syntax (describe, it, expect)
- MUST be fully runnable code

Return ONLY the final test file.

Code to test:
{data.code}
"""

    try:
        # -------------------------
        # CALL OLLAMA
        # -------------------------
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-coder",   # BEST for code
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,   # makes output strict
                    "num_predict": 400
                }
            },
            timeout=300
        )

        # -------------------------
        # HANDLE ERRORS SAFELY
        # -------------------------
        if response.status_code != 200:
            return {
                "result": f"ERROR FROM OLLAMA: {response.text}"
            }

        result = response.json().get("response", "")

        # -------------------------
        # CLEAN OUTPUT (VERY IMPORTANT)
        # -------------------------
        result = result.replace("```javascript", "")
        result = result.replace("```js", "")
        result = result.replace("```", "")

        return {
            "result": result.strip()
        }

    except Exception as e:
        return {
            "result": f"SERVER ERROR: {str(e)}"
        }