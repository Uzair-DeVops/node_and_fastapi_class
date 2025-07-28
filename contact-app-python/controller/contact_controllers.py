from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from motor.motor_asyncio import AsyncIOMotorCollection
from database import get_contacts_collection
from fastapi import Depends
from models.contact_model import Contact    
from bson import ObjectId
from fastapi.responses import RedirectResponse
from services.contact_services import get_contacts, get_contact_by_id, add_contact, update_contact, delete_contact
templates = Jinja2Templates(directory="templates")


# render controllers
async def home_page(request: Request, collection: AsyncIOMotorCollection):
    contacts = await get_contacts(request, collection)
    return templates.TemplateResponse("home.html", {"request": request, "contacts": contacts})

async def update_contact_page(request: Request, collection: AsyncIOMotorCollection, id: str):
    contact = await get_contact_by_id(request, collection, id)
    return templates.TemplateResponse("update-contact.html", {"request": request, "contact": contact})

async def add_contact_page(request: Request, collection: AsyncIOMotorCollection):
    return templates.TemplateResponse("add-contact.html", {"request": request})

async def show_contact_page(request: Request, collection: AsyncIOMotorCollection, id: str):
    contact = await get_contact_by_id(request, collection, id)
    return templates.TemplateResponse("show-contact.html", {"request": request, "contact": contact})





# redirect controllers
async def add_contact_redirect(request: Request, collection: AsyncIOMotorCollection):
    contact = await add_contact(request, collection)
    return RedirectResponse("/", status_code=302)

async def update_contact_redirect(request: Request, collection: AsyncIOMotorCollection):
    contact = await update_contact(request, collection)
    return RedirectResponse("/", status_code=302)

async def delete_contact_redirect(request: Request, collection: AsyncIOMotorCollection, id: str):
    contact = await delete_contact(request, collection, id)
    return RedirectResponse("/", status_code=302)