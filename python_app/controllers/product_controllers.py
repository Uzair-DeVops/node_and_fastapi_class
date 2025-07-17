import json
from fastapi import  Request , Response
import asyncio
with open("data.json", "r") as f:
    data = json.load(f)



async def read_all_products(request: Request, response: Response):
    return data


async def read_product_by_id(request: Request, response: Response):
    id = request.path_params["id"]
    # id = int(id)
    for product in data:
        if product["id"] == id:
            return product
        else:
            return {"message": "Product not found"}
        




async def create_product(request: Request, response: Response):
    new_product = await request.json()
    # generate id
    new_product["id"] = len(data) + 1
    data.append(new_product)
    return new_product


async def update_product_by_id(request: Request, response: Response):
    id = int(request.path_params["id"])
    updated_product = await request.json()
    for product in data:
        if product["id"] == id:
            product = dict(product, **updated_product)
            return product




async def delete_product_by_id(request: Request, response: Response):
    id = int(request.path_params["id"])
    for product in data:
        if product["id"] == id:
            data.remove(product)
            return {"message": "Product deleted"}