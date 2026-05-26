import os
from .python_analyzer import analyze_python
from .javascript_analyzer import analyze_javascript
from .java_analyzer import analyze_java

SUPPORTED = {"python", "javascript", "java"}

def analyze_code(language, code):
    language = language.lower().strip()
    max_len = int(os.getenv("MAX_CODE_LENGTH", "50000"))
    if not code or not code.strip():
        raise ValueError("Code input cannot be empty.")
    if len(code) > max_len:
        raise ValueError(f"Code length exceeds maximum limit of {max_len}.")
    if language not in SUPPORTED:
        raise ValueError("Unsupported language.")
    if language == "python":
        return analyze_python(code)
    if language == "javascript":
        return analyze_javascript(code)
    return analyze_java(code)

def build_repository_summary(reviews):
    if not reviews:
        return {"files_analyzed":0,"average_quality_score":0,"top_bugs":[],"top_security_issues":[],"most_complex_files":[],"overall_recommendations":["No analyzable files were found."]}
    avg = sum(r.get("quality_score", 0) for r in reviews) / len(reviews)
    bugs, security, complex_files = [], [], []
    for r in reviews:
        file_name = r.get("file_name", "unknown")
        for bug in r.get("bugs", [])[:2]:
            bugs.append({"file": file_name, "title": bug.get("title"), "severity": bug.get("severity")})
        for sec in r.get("security_issues", [])[:2]:
            security.append({"file": file_name, "title": sec.get("title"), "severity": sec.get("severity")})
        complex_files.append({"file": file_name, "complexity_score": r.get("complexity_score", 0)})
    return {
        "files_analyzed": len(reviews),
        "average_quality_score": round(avg, 2),
        "top_bugs": bugs[:10],
        "top_security_issues": security[:10],
        "most_complex_files": sorted(complex_files, key=lambda x: x["complexity_score"], reverse=True)[:5],
        "overall_recommendations": ["Fix high-severity security findings first.", "Refactor files with high complexity.", "Add tests for critical modules.", "Remove debug statements and hardcoded values."]
    }
