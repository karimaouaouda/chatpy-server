import Core
from Core.Database import DB


def login(payload):
    user = DB.table("users").find("email", payload["email"])
    if user is not None:
        if user["password"] == payload["password"]:
            return user
        else:
            return "invalid password"
    else:
        return "invalid email not found"


def register(payload):
    query = DB.table('users').insert(payload)
    if query is None:
        return DB.table('users').find("email", payload["email"])
    else:
        return "Email already registered"


def logout():
    cursor = Core.cursor()
