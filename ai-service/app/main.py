from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import CodeAnalyzeRequest, AnalyzeResponse, RepositorySummaryRequest
from .analyzer import analyze_code, build_repository_summary

app = FastAPI(title="CodeGuard AI Static Analysis Service")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def health():
    return {"message": "CodeGuard AI service is running"}

@app.post("/analyze-code", response_model=AnalyzeResponse)
def analyze(payload: CodeAnalyzeRequest):
    try:
        return analyze_code(payload.language, payload.code)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception:
        raise HTTPException(status_code=500, detail="Analysis service failed safely.")

@app.post("/analyze-repository-summary")
def repository_summary(payload: RepositorySummaryRequest):
    return build_repository_summary(payload.reviews)
