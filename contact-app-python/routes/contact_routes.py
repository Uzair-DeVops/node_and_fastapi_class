from fastapi import APIRouter, Depends, Request, Path   
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controller.contact_controllers import home_page, add_contact_page, update_contact_page, show_contact_page, get_contacts, add_contact, update_contact, delete_contact, get_contact_by_id ,add_contact_redirect, update_contact_redirect, delete_contact_redirect    
from motor.motor_asyncio import AsyncIOMotorCollection
from database import get_contacts_collection
from models.contact_model import Contact
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# render routes for contact page
@router.get("/")
async def home_page_route(request: Request, collection: AsyncIOMotorCollection = Depends(get_contacts_collection)):
    return await home_page(request, collection)

@router.get("/add-contact")
async def add_contact_page_route(request: Request, collection: AsyncIOMotorCollection = Depends(get_contacts_collection)):
    return await add_contact_page(request, collection)

@router.get("/update-contact/{id}")
async def update_contact_page_route(request: Request, id: str, collection: AsyncIOMotorCollection = Depends(get_contacts_collection)):
    return await update_contact_page(request, collection, id)

@router.get("/show-contact/{id}")
async def show_contact_page_route(request: Request, id: str, collection: AsyncIOMotorCollection = Depends(get_contacts_collection)):
    return await show_contact_page(request, collection , id)

@router.get("/delete-contact/{id}")
async def delete_contact_route(request: Request, id: str, collection: AsyncIOMotorCollection = Depends(get_contacts_collection)):
    return await delete_contact_redirect(request, collection, id)






@router.post("/add-contact")
async def add_contact_route(request: Request,  collection: AsyncIOMotorCollection = Depends(get_contacts_collection)):
    return await add_contact_redirect(request, collection)

@router.post("/update-contact/{id}")
async def update_contact_route(request: Request, collection: AsyncIOMotorCollection = Depends(get_contacts_collection)):
    return await update_contact_redirect(request, collection)
