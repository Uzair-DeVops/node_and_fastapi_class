from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from dotenv import load_dotenv
import os
from typing import AsyncGenerator
from fastapi import Request, FastAPI

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = "my_database_python"

async def connect_database(app: FastAPI):
    """Connect to the database and store in app.state"""
    try:
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[DATABASE_NAME]
        # Test the connection
        await client.admin.command('ping')
        
        # Store in app.state
        app.state.mongodb_client = client
        app.state.mongodb_db = db        
        print("Database connected successfully")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise e

async def close_database(app: FastAPI):
    """Close the database connection"""
    if hasattr(app.state, 'mongodb_client'):
        app.state.mongodb_client.close()
        print("Database disconnected successfully")













# FastAPI Dependencies
async def get_db(request: Request) -> AsyncGenerator[AsyncIOMotorDatabase, None]:
    """Dependency to get database instance"""
    database = request.app.state.mongodb_db
    try:
        yield database
    finally:
        pass

async def get_contacts_collection(request: Request) -> AsyncGenerator:
    """Dependency to get contacts collection"""
    collection = request.app.state.mongodb_db["contacts"]
    try:
        yield collection
    finally:
        pass