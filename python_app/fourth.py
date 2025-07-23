from fastapi import FastAPI , Request , Depends
from fastapi.responses import JSONResponse
import uvicorn
from models.product import Product
from database import connect_to_database
from controllers.product_controllers import read_all_products

from bson import ObjectId 



Table = connect_to_database()


app = FastAPI()

app.state.Table = Table
# Table = connect_to_database()



def get_table():
    return app.state.Table

# get products
@app.get("/products")
async def get_all_products_route(Table = Depends(get_table)): 
    return await read_all_products(Table)
   

# TODO

# # get single product
# @app.get("/products/{id}")
# async def get_single_product(id : str):
#     product = Table.find_one({"_id": ObjectId(id)})
#     serialize_mongo(product)
#     return JSONResponse(content = product , status_code=200)



# @app.post("/products")
# async def create_new_product(product : Product):
#     product = product.model_dump()
#     Table.insert_one(product)
#     serialize_mongo(product)
#     return JSONResponse(content = product , status_code=201)




# # update product
# @app.put("/products/{id}")
# async def update_product(id : str , product : Product):
#     product = product.model_dump()
#     Table.update_one({"_id": ObjectId(id)}, {"$set": product})
#     newproduct = Table.find_one({"_id": ObjectId(id)})
#     serialize_mongo(newproduct)
#     return JSONResponse(content = product , status_code=200)


# # delete 
# @app.delete("/products/{id}")
# async def delete_product(id : str):
#     Table.delete_one({"_id": ObjectId(id)})
#     return JSONResponse(content = {"message": "Product deleted"} , status_code=200)



if __name__ == "__main__":
    uvicorn.run("fourth:app", host="0.0.0", port=3500 , reload=True)
    print("the sever is running on link http://127.0.0.1:3500")






















































































































































# from fastapi import FastAPI ,Request
# import uvicorn
# from database import connect_to_database
# from pydantic import BaseModel, Field 
# from typing import Optional
# from fastapi.responses import JSONResponse
# from bson import ObjectId

# app = FastAPI()


# collection = connect_to_database()


# class Product(BaseModel):
#     name: str = Field(...)
#     price: float
#     category: Optional[str] = None  # not required now





# def serialize_mongo(doc):
#     doc["id"] = str(doc["_id"])
#     del doc["_id"]
#     return doc



# # create product 
# @app.post("/products" )
# async def create_product(product: Product):
#     new_product = product.model_dump()
#     result = collection.insert_one(new_product)
#     # find newly created product
#     new_product = collection.find_one({"_id": result.inserted_id})
#     return JSONResponse(content=serialize_mongo(new_product), status_code=201)



# # read all products
# @app.get("/products")
# async def read_all_products():
#     products = []
#     for doc in collection.find():
#         products.append(serialize_mongo(doc))
#     return products


# # read product by id
# @app.get("/products/{id}")
# async def read_product(request : Request):
#     id = request.path_params["id"]
#     product = collection.find_one({"_id": ObjectId(id)})
#     if product:
#         return serialize_mongo(product)
#     else:
#         return JSONResponse(content={"message": "Product not found"}, status_code=404)
    


# #update product by id
# # update_product_by_id
# @app.put("/products/{id}")
# async def update_product(request: Request, product: Product):
#     id = request.path_params["id"]
#     updated_product = product.model_dump()
#     result = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_product})
#     if result.modified_count > 0:
#         updated_product = collection.find_one({"_id": ObjectId(id)})
#         return serialize_mongo(updated_product)
#     else:
#         return JSONResponse(content={"message": "Product not found"}, status_code=404)
    

# # delete product by id

# @app.delete("/products/{id}")
# async def delete_product(request: Request):
#     id = request.path_params["id"]
#     result = collection.delete_one({"_id": ObjectId(id)})
#     print(result)
#     if result.deleted_count > 0:
#         return JSONResponse(content={"message": "Product deleted"}, status_code=200)
#     else:
#         return JSONResponse(content={"message": "Product not found"}, status_code=404)
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0", port=3500)