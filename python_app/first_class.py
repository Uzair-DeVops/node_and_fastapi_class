from fastapi import FastAPI
import uvicorn
from fastapi import Request, Response

app = FastAPI()

@app.get("/")
async def read_root(request: Request, response: Response):
    print(request.headers)
    print(request.query_params)
    print(request.path_params)
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/about")
async def read_about():
    return {"message": "This is the about page."}


@app.get("/contact")
async def read_contact():
    return {"message": "This is the contact page."}

@app.get("/hello")
async def read_hello():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0", port=8000)








