from fastapi import FastAPI
from routers import metrics, aws
app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utilities for monitoring metrics and logs",
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def hello():
    return {"message": "Hello, This is first API for DevOps Utilities"}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")


