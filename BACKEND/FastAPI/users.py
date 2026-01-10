from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciar el server: uvicorn users:app --reload
# Detener el server: Ctrl + C

# Entidad User

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1,name="Brais", surname="Moure", url="https://moure.dev", age=35),
                User(id=2, name="Moure", surname="Dev", url="https://mouredev.com ", age=30),
                User(id=3, name="Fran", surname="Junquero", url="https://marru.com", age=52)]



@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 30},
            {"name": "Fran", "surname": "Junquero", "url": "https://marru.com", "age": 52}]

@app.get("/users")
async def users():
    return users_list

# Path

@app.get("/users/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return { "error": "no se ha encontrado el usuario" }
    
# Query

@app.get("/userquery/")
async def userquery(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return { "error": "no se ha encontrado el usuario" }