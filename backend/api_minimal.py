from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import dashboard, problems, worksheets
from database import get_database

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(dashboard.router, prefix="/api")
app.include_router(problems.router, prefix="/api")
app.include_router(worksheets.router, prefix="/api")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Olympiad Math Archive API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
