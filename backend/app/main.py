from fastapi import FastAPI

app = FastAPI(
    title="TrustAid API",
    description="Backend API for TrustAid donation transparency platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "TrustAid API is running",
        "status": "success",
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "TrustAid Backend",
    }