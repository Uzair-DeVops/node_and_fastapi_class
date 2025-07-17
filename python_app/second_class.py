import json
from fastapi import FastAPI 
import uvicorn
from routes.product_routes import router as product_router
app = FastAPI()



app.include_router(prefix="/products" ,router = product_router)









if __name__ == "__main__":
    uvicorn.run("second_class:app", port=8000 , reload=True)