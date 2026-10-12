from fastapi import FastAPI
app = FastAPI(title="Employee API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
