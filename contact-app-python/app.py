from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.contact_routes import router as contact_router
from database import connect_database, close_database

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup_event():
    await connect_database(app)

@app.on_event("shutdown")
async def shutdown_event():
    await close_database(app)

app.include_router(contact_router)












