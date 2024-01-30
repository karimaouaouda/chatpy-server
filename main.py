from fastapi import FastAPI, Body
from Core.Controllers import UserController
from Core.Controllers.GPT import GPT
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/login", status_code=200)
async def login(email: str = Body(...), password: str = Body(...)):
    data = UserController.login(email, password)
    print(data)
    if data is not None:
        return {"user": email, "password": password, "status": True}
    return {"message": "Invalid credentials", "status": False}


@app.post("/send", status_code=200)
async def send(message: str = Body(...)):
    gpt = GPT(message=message)

    if gpt.ready:
        return {"content": gpt.content()}
