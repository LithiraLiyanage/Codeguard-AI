import re
from .scoring import quality_score, maintainability_score

SECRET = re.compile(r"(password|secret|token|apiKey|privateKey)\s*=\s*\"[^\"]+\"", re.I)

def analyze_java(code):
    bugs, security, smells = [], [], []
    lines = code.splitlines()
    for i, line in enumerate(lines, 1):
        if "System.out.println" in line:
            smells.append({"title":"System.out.println found","description":"Console printing is not ideal for production.","recommendation":"Use a logging framework."})
        if SECRET.search(line):
            security.append({"title":"Possible hardcoded credential","severity":"high","line":i,"description":"Credential-like value appears hardcoded.","safeFix":"Move secrets to secure config."})
        if re.search(r"public\s+\w+\s+\w+\s*;", line):
            smells.append({"title":"Public mutable field","description":"Public fields break encapsulation.","recommendation":"Use private fields and accessors."})
    if re.search(r"catch\s*\([^)]*\)\s*\{\s*\}", code, re.S):
        bugs.append({"title":"Empty catch block","severity":"medium","line":1,"description":"Empty catch blocks hide errors.","recommendation":"Handle or log exceptions."})
    method_count = len(re.findall(r"(public|private|protected)\s+[\w<>\[\]]+\s+\w+\s*\(", code))
    complexity = min(100, int((len(lines)/4) + method_count*5))
    if len(lines) > 200:
        smells.append({"title":"Large Java file","description":"Class may have too many responsibilities.","recommendation":"Split into smaller classes."})
    return {
        "quality_score": quality_score(bugs, security, smells, complexity),
        "maintainability_score": maintainability_score(smells, complexity, len(lines)),
        "complexity_score": complexity,
        "summary": "Java analysis completed using static pattern checks.",
        "bugs": bugs,
        "security_issues": security,
        "code_smells": smells,
        "refactor_suggestions": ["Use dependency injection.", "Replace magic values with constants.", "Use specific exception handling.", "Add input validation."],
        "best_practices": ["Use logging framework.", "Keep classes single-purpose.", "Write unit tests.", "Prefer immutability."],
        "complexity_explanation": f"Complexity score is {complexity}/100.",
        "improved_code": ""
    }
