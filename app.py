from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database setup
DATABASE_URL = "sqlite:///./voting_system.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    party = Column(String)
    bio = Column(String)

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User")
    candidate = relationship("Candidate")

Base.metadata.create_all(bind=engine)

# Seed data
def seed_data():
    db = SessionLocal()
    if not db.query(User).first():
        user1 = User(username="admin", password_hash="hashed_password", role="admin")
        user2 = User(username="voter1", password_hash="hashed_password", role="voter")
        db.add(user1)
        db.add(user2)
    if not db.query(Candidate).first():
        candidate1 = Candidate(name="Alice", party="Party A", bio="Experienced politician")
        candidate2 = Candidate(name="Bob", party="Party B", bio="Newcomer with fresh ideas")
        db.add(candidate1)
        db.add(candidate2)
    db.commit()
    db.close()

seed_data()

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        return f.read()

@app.get("/vote", response_class=HTMLResponse)
async def vote_page():
    with open("templates/vote.html") as f:
        return f.read()

@app.get("/results", response_class=HTMLResponse)
async def results_page():
    with open("templates/results.html") as f:
        return f.read()

@app.get("/login", response_class=HTMLResponse)
async def login_page():
    with open("templates/login.html") as f:
        return f.read()

@app.get("/admin", response_class=HTMLResponse)
async def admin_page():
    with open("templates/admin.html") as f:
        return f.read()

@app.get("/api/candidates")
async def get_candidates():
    db = SessionLocal()
    candidates = db.query(Candidate).all()
    db.close()
    return candidates

@app.post("/api/vote")
async def cast_vote(user_id: int, candidate_id: int):
    db = SessionLocal()
    vote = Vote(user_id=user_id, candidate_id=candidate_id)
    db.add(vote)
    db.commit()
    db.close()
    return {"message": "Vote cast successfully"}

@app.get("/api/results")
async def get_results():
    db = SessionLocal()
    results = db.query(Vote.candidate_id, Candidate.name, Candidate.party, func.count(Vote.id).label("vote_count")).join(Candidate).group_by(Vote.candidate_id).all()
    db.close()
    return results

@app.post("/api/login")
async def login(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    if user and user.password_hash == "hashed_password":  # Simplified for demonstration
        return {"message": "Login successful", "token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
