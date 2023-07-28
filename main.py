import random
from typing import Union

from fastapi import FastAPI

from item import Item
from responseVo import ResponseVo

app = FastAPI()


@app.get("/")
def hello():
    return {"info": "Hello FastApi"}


@app.get("/item/{item_id}", response_model=ResponseVo[str])
def item(item_id: str, query: Union[str, None] = None) -> ResponseVo[str]:
    return {"code": 0, "msg": "操作成功", "data": item_id + (query if query is not None else "")}


@app.post("/item", response_model=ResponseVo[int])
def create_item(one_item: Item):
    one_item.id = random.randint(3, 4)
    return {"code": 0, "msg": "保存成功", "data": one_item.id}


@app.put("/item/{item_id}", response_model=ResponseVo[Item])
def update_item(item_id: str, one_item: Item) -> ResponseVo[Item]:
    one_item.id = item_id
    return {"code": 0, "msg": "更新成功", "data": one_item}


@app.delete("/item/{item_id}", response_model=ResponseVo[None])
def delete_item(item_id: str) -> ResponseVo[None]:
    return {"code": 0, "msg": "删除成功", "data": None}


