from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class CodeAnalyzeRequest(BaseModel):
    language: str = Field(..., min_length=1)
    code: str = Field(..., min_length=1)
    file_name: Optional[str] = ""

class Issue(BaseModel):
    title: str
    severity: str
    line: int
    description: str
    recommendation: Optional[str] = None
    safeFix: Optional[str] = None

class CodeSmell(BaseModel):
    title: str
    description: str
    recommendation: str

class AnalyzeResponse(BaseModel):
    quality_score: int
    maintainability_score: int
    complexity_score: int
    summary: str
    bugs: List[Issue]
    security_issues: List[Issue]
    code_smells: List[CodeSmell]
    refactor_suggestions: List[str]
    best_practices: List[str]
    complexity_explanation: str
    improved_code: str = ""

class RepositorySummaryRequest(BaseModel):
    reviews: List[Dict[str, Any]]
