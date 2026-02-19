from fastapi import FastAPI
from routes.User_routes import router as user_router
from db import engine
from models import Base

app = FastAPI()

# Include routes
app.include_router(user_router)

# Create tables on startup
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():  
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[0.0.0.0]", port=8000)