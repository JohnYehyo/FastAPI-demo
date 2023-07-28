from typing import Generic, TypeVar, Optional
from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class ResponseVo(GenericModel, Generic[DataT]):
    """返回结果对象"""
    code: int
    msg: str
    data: Optional[DataT] = None
