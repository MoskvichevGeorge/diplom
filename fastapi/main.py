from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def home():
    return {"message" : "Hello,FastAPI!"}

@app.get('/about')
async def hello():
    return {'message' : 'This is the About page.'}

@app.get('/greet/{name}')
async def greet(name: str):
    return {'message': f'Hello,{name}!'}
class Item(BaseModel):
    name: str
    price : float
    is_avaiable: bool= True

@app.post('/items/')
async def create_item(item: Item, item_name=None, item_price=None):
    return {'item_name': item_name, 'item_price': item_price, 'is_available' :item.is_avialable}