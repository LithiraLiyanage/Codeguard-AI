# System Architecture

Frontend sends authenticated requests to the Express backend. Backend validates inputs, handles uploads and GitHub repository cloning, saves review history in MongoDB, and forwards source code to the Python FastAPI microservice. The AI microservice performs defensive static analysis using AST and rule-based checks.
