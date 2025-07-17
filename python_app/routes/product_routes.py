from fastapi import APIRouter , Request , Response
import json
from controllers.product_controllers import read_all_products , read_product_by_id ,create_product ,delete_product_by_id,update_product_by_id
from fastapi.responses import JSONResponse , HTMLResponse , PlainTextResponse



router = APIRouter()





@router.get("")
async def read_products(request: Request, response: Response):
    data = await read_all_products(request, response)
    return data


@router.get("/{id}")
async def read_sinlge_product(request: Request, response: Response):
    data = await read_product_by_id(request, response)
    return data    


@router.post("")
async def create_new_product(request: Request, response: Response):
    data = await create_product(request, response)
    return data


@router.put("/{id}")
async def update_product(request: Request, response: Response):
    data = await update_product_by_id(request, response)
    return data

@router.delete("/{id}")
async def delete_product(request: Request, response: Response):
    data = await delete_product_by_id(request, response)
    return data 