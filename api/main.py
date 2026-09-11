from fastapi import FastAPI

from api.routers import risk, claim, monitoring

app = FastAPI(title="Healthcare ML API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Healthcare ML API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# Registering Routes
app.include_router(risk.router, prefix="/predict", tags=["Risk Score Prediction"])
app.include_router(claim.router, prefix="/predict", tags=["Claim Status Prediction"])
app.include_router(monitoring.router, prefix="/monitor", tags=["Monitoring"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)