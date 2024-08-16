from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int | None = None
    phone: str | None = None