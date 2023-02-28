from typing import Union
from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class RequestDataclass:
    file_name: str
    cmd1: str
    value1: Union[str, int]
    cmd2: str
    value2: Union[str, int]


RequestSchema = marshmallow_dataclass.class_schema(RequestDataclass)
