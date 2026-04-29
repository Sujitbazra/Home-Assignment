# Stage 1: Builder
    FROM python:3.11-slim AS builder

    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --user -r requirements.txt
    
    # Stage 2: Production
    FROM python:3.11-alpine
    
    RUN adduser -D appuser
    WORKDIR /app
    
    COPY --from=builder /root/.local /root/.local
    COPY app.py .
    
    ENV PATH=/root/.local/bin:$PATH
    
    USER appuser
    
    EXPOSE 5000
    
    HEALTHCHECK CMD wget -qO- http://localhost:5000/health || exit 1
    
    CMD ["python", "app.py"]