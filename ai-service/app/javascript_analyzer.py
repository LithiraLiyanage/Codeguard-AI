import re
from .scoring import quality_score, maintainability_score

SECRET = re.compile(r"(password|secret|token|apiKey|api_key|privateKey)\s*[:=]\s*['\"][^'\"]+['\"]", re.I)

def analyze_javascript(code):
    bugs, security, smells = [], [], []
    lines = code.splitlines()
    for i, line in enumerate(lines, 1):
        if "console.log" in line:
            smells.append({"title":"console.log found","description":"Debug logging appears in code.","recommendation":"Remove logs or use a logging utility."})
        if re.search(r"\bvar\b", line):
            smells.append({"title":"var usage","description":"var has function scope and may create bugs.","recommendation":"Use const or let."})
        if re.search(r"[^=!]==[^=]", line) or re.search(r"!=[^=]", line):
            bugs.append({"title":"Loose equality operator","severity":"low","line":i,"description":"Loose equality may cause type coercion.","recommendation":"Use === or !==."})
        if "eval(" in line:
            security.append({"title":"Use of eval()","severity":"high","line":i,"description":"eval executes dynamic code and is risky.","safeFix":"Avoid eval and use explicit logic."})
        if "dangerouslySetInnerHTML" in line or ".innerHTML" in line:
            security.append({"title":"Unsafe HTML injection pattern","severity":"high","line":i,"description":"Raw HTML injection may cause XSS risks.","safeFix":"Avoid raw HTML injection and sanitize content."})
        if SECRET.search(line):
            security.append({"title":"Possible hardcoded secret","severity":"high","line":i,"description":"Credential-like value appears hardcoded.","safeFix":"Move secrets to environment variables."})
    if "async" in code and "try" not in code and ".catch(" not in code:
        bugs.append({"title":"Async code may lack error handling","severity":"medium","line":1,"description":"Async operations should handle failures.","recommendation":"Use try/catch or .catch()."})
    fn_count = len(re.findall(r"function\s+\w+|\=\s*\([^)]*\)\s*=>|\=\s*\w+\s*=>", code))
    complexity = min(100, int((len(lines)/4) + fn_count*5))
    if len(lines) > 180:
        smells.append({"title":"Large file","description":"File may combine many responsibilities.","recommendation":"Split into smaller modules."})
    return {
        "quality_score": quality_score(bugs, security, smells, complexity),
        "maintainability_score": maintainability_score(smells, complexity, len(lines)),
        "complexity_score": complexity,
        "summary": "JavaScript/TypeScript analysis completed using defensive static checks.",
        "bugs": bugs,
        "security_issues": security,
        "code_smells": smells,
        "refactor_suggestions": ["Use const by default.", "Extract repeated logic.", "Validate external input.", "Add unit tests."],
        "best_practices": ["Use strict equality.", "Keep functions short.", "Avoid hardcoded configuration.", "Use meaningful names."],
        "complexity_explanation": f"Complexity score is {complexity}/100.",
        "improved_code": ""
    }
