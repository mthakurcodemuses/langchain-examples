from typing import List
from pydantic.v1 import BaseModel


class DescribeTableArgsSchema(BaseModel):
    table_names: List[str]
