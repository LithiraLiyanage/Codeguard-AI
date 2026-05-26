import ast, re
from radon.complexity import cc_visit
from .scoring import quality_score, maintainability_score

SECRET = re.compile(r"(password|secret|token|api_key|apikey|private_key)\s*=\s*['\"][^'\"]+['\"]", re.I)

class Visitor(ast.NodeVisitor):
    def __init__(self):
        self.bugs = []
        self.security = []
        self.smells = []
    def visit_Call(self, node):
        name = node.func.id if isinstance(node.func, ast.Name) else ""
        if name == "eval":
            self.security.append({"title":"Use of eval()","severity":"high","line":node.lineno,"description":"eval() executes dynamic code and can create security risks.","safeFix":"Avoid eval. Use safe parsing or explicit logic."})
        if name == "exec":
            self.security.append({"title":"Use of exec()","severity":"high","line":node.lineno,"description":"exec() executes dynamic code and can create security risks.","safeFix":"Avoid exec and refactor into explicit functions."})
        self.generic_visit(node)
    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.bugs.append({"title":"Bare except block","severity":"medium","line":node.lineno,"description":"Bare except catches all exceptions and hides unexpected errors.","recommendation":"Catch specific exception types."})
        if not node.body or all(isinstance(stmt, ast.Pass) for stmt in node.body):
            self.bugs.append({"title":"Empty exception handler","severity":"medium","line":node.lineno,"description":"Empty exception handlers hide errors.","recommendation":"Log or handle the exception."})
        self.generic_visit(node)
    def visit_FunctionDef(self, node):
        if len(node.body) > 35:
            self.smells.append({"title":"Long function","description":f"Function {node.name} is long.","recommendation":"Split into smaller functions."})
        if not node.returns:
            self.smells.append({"title":"Missing return type hint","description":f"Function {node.name} has no return type hint.","recommendation":"Add type hints."})
        self.generic_visit(node)

def analyze_python(code):
    bugs, security, smells = [], [], []
    lines = code.splitlines()
    for i, line in enumerate(lines, 1):
        if SECRET.search(line):
            security.append({"title":"Possible hardcoded secret","severity":"high","line":i,"description":"Credential-like value appears hardcoded.","safeFix":"Move secrets to environment variables."})
    try:
        tree = ast.parse(code)
        visitor = Visitor()
        visitor.visit(tree)
        bugs += visitor.bugs
        security += visitor.security
        smells += visitor.smells
    except SyntaxError as e:
        bugs.append({"title":"Python syntax error","severity":"high","line":e.lineno or 1,"description":e.msg,"recommendation":"Fix syntax error first."})
    complexity = min(100, max(5, int(len(lines)/3)))
    try:
        blocks = cc_visit(code)
        if blocks:
            complexity = min(100, int((sum(b.complexity for b in blocks)/len(blocks))*12))
    except Exception:
        pass
    if len(lines) > 150:
        smells.append({"title":"Large file","description":"File may have too many responsibilities.","recommendation":"Split into modules."})
    return {
        "quality_score": quality_score(bugs, security, smells, complexity),
        "maintainability_score": maintainability_score(smells, complexity, len(lines)),
        "complexity_score": complexity,
        "summary": "Python code analysis completed using AST parsing and rule-based checks.",
        "bugs": bugs,
        "security_issues": security,
        "code_smells": smells,
        "refactor_suggestions": ["Extract repeated logic into helper functions.", "Add clear error handling.", "Use environment variables for configuration."],
        "best_practices": ["Use type hints.", "Write unit tests.", "Keep functions focused.", "Validate user input."],
        "complexity_explanation": f"Complexity score is {complexity}/100.",
        "improved_code": ""
    }
