





































































































# from fastapi import FastAPI, Request
# import uvicorn
# from fastapi.templating import Jinja2Templates
# import json

# app = FastAPI()

# with open("productsData.json", "r") as f:
#     data = json.load(f)

# templates = Jinja2Templates(directory="views")

# @app.get("/")
# async def read_root(request: Request):
#     return templates.TemplateResponse("products.html", {"request": request , "products": data["products"]})




# if __name__ == "__main__":
#     uvicorn.run("third_class:app", port=8000 , reload=True)