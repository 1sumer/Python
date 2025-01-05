from fastapi import FastAPI
from app.routes import user_routes
from app.database import create_db_and_tables

app = FastAPI(title="User Management API")

# Include user routes
app.include_router(user_routes.router)

@app.on_event("startup")
async def startup_event():
    # Initialize database on startup
    create_db_and_tables()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the User Management API!"}