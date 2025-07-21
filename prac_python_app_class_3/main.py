from fastapi import FastAPI ,Response , Request
from fastapi.templating import Jinja2Templates
import uvicorn
import json

app = FastAPI()

with open("productsData.json", "r") as f:
    data = json.load(f)

templates = Jinja2Templates(directory="views")



@app.get("/")
async def read_root(request: Request, response: Response):
    return templates.TemplateResponse("products.html", {"request": request , "products": data})





if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0", port=8000 , reload=True)