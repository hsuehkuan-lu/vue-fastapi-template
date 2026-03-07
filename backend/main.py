from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine
from dependencies import get_db
import models

# Ensure tables are created (though alembic handles this now, good for simple tests if we didn't)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vue FastAPI Template")

# Allow CORS for local development and from the frontend container
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI Backend!"}

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.post("/api/users")
def create_user(email: str, db: Session = Depends(get_db)):
    db_user = models.User(email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/api/users")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users
