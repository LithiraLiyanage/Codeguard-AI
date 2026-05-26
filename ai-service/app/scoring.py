def deduction(severity: str) -> int:
    return 15 if severity == "high" else 8 if severity == "medium" else 4

def quality_score(bugs, security, smells, complexity):
    score = 100
    for item in bugs + security:
        score -= deduction(item.get("severity", "low"))
    score -= len(smells) * 3
    if complexity > 70:
        score -= 12
    elif complexity > 45:
        score -= 6
    return max(0, min(100, int(score)))

def maintainability_score(smells, complexity, lines):
    score = 100 - len(smells) * 7
    if lines > 300:
        score -= 10
    elif lines > 150:
        score -= 5
    if complexity > 70:
        score -= 15
    elif complexity > 45:
        score -= 8
    return max(0, min(100, int(score)))
