from fastapi import FastAPI, Body
from Core.Controllers import UserController
from Core.Controllers.GPT import GPT
from Core.Database import DB

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/login", status_code=200)
async def login(payload: dict = Body(...)):
    user = UserController.login(payload)
    if type(user) is not str:
        return {"user": user, "status": "success"}
    return {"message": f"{user}", "status": "fail"}


@app.post("/send", status_code=200)
async def send(payload: dict = Body(...)):
    gpt = GPT(message=payload['message'])

    # MessageController.save(msg=message, response=gpt.content(), token="token")

    if gpt.ready:
        return {"content": gpt.content()}



@app.post("/send_message", status_code=200)
async def send_message(payload: dict = Body(...)):
    message = payload['message']
    feel = payload['feel']
    parts = feel.split("_")
    emotion = parts[0] if len(parts) == 1 else parts[1]
    sex = parts[0] if len(parts) == 2 else "unknown"
    print(emotion)
    return {"content": f"why you are {payload['feel']} today? "}


@app.post("/register", status_code=200)
async def send_message(payload: dict = Body(...)):
    user = UserController.register(payload)
    if type(user) is not str:
        return {"status": "success", "user": user}
    else:
        return {"status": "fail", "message": f"{user}"}
