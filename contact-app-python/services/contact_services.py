from fastapi import Request
from models.contact_model import Contact
from bson import ObjectId
from fastapi.responses import RedirectResponse
from motor.motor_asyncio import AsyncIOMotorCollection


  # function to convert ObjectId to str 
def convert_object_id_to_str(contact: dict):
    contact["_id"] = str(contact["_id"])
    return contact





# get all contacts
async def get_contacts(request: Request, collection: AsyncIOMotorCollection):
    contacts = await collection.find().to_list(1000)
    return [convert_object_id_to_str(contact) for contact in contacts]


# get contact by id
async def get_contact_by_id(request: Request, collection: AsyncIOMotorCollection, id: str):
    contact = await collection.find_one({"_id": ObjectId(id)})
    return convert_object_id_to_str(contact)

# add contact
async def add_contact(request: Request, collection: AsyncIOMotorCollection):
    data = await request.form()
    contact = Contact(first_name=data["first_name"], last_name=data["last_name"], email=data["email"], phone=data["phone"], address=data["address"])
    contact_dict = contact.model_dump()
    new_contact = await collection.insert_one(contact_dict)
    contact = await get_contact_by_id(request, collection, new_contact.inserted_id)
    return convert_object_id_to_str(contact)

# update contact by id
async def update_contact(request: Request, collection: AsyncIOMotorCollection):
    # Only include fields that are not None
    id = request.path_params["id"]
    data = await request.form()
    contact = Contact(first_name=data["first_name"], last_name=data["last_name"], email=data["email"], phone=data["phone"], address=data["address"])    
    contact_dict = contact.model_dump()
    await collection.update_one({"_id": ObjectId(id)}, {"$set": contact_dict})
    return RedirectResponse("/", status_code=302)



# delete contact by id
async def delete_contact(request: Request, collection: AsyncIOMotorCollection, id: str):
    await collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Contact deleted successfully"}