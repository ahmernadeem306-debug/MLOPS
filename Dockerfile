# 1. Base Image: Python 3.10 operating system ke sath download karo
FROM python:3.10-slim

# 2. Workspace: Container ke andar ek folder banayein jahan code rakhenge
WORKDIR /app

# 3. Dependencies: FastAPI aur Uvicorn install karo
RUN pip install fastapi uvicorn

# 4. Copy Code: Hamari machine ka main.py file container mein copy karo
COPY main.py .

# 5. Command: Jab dabba start ho, toh server automatically run ho jaye
CMD ["python", "main.py"]
