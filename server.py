from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Модель данных для POST-запроса
class Item(BaseModel):
    name: str
    price: float

# Главная страница
@app.get("/")
def read_root():
    return {"message": "FastAPI сервер работает!"}

# Пример GET-запроса
@app.get("/api/info")
def get_info():
    return {"status": "ok", "data": "Это пример API"}

# Пример POST-запроса
@app.post("/api/items")
def create_item(item: Item):
    return {"received_item": item.dict()}

# Пример обработки query-параметров
@app.get("/api/search")
def search(q: str):
    return {"query": q, "result": f"Вы искали: {q}"}
