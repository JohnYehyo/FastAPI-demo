from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    """项目对象"""
    id: int
    name: str
    price: str
    is_offer: Union[bool, None] = None
