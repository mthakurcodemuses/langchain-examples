from pydantic.v1 import BaseModel


class RunQueryArgsSchema(BaseModel):
    query: str
