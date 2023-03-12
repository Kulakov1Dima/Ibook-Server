from pydantic import BaseModel

class Auth(BaseModel):
    name: str
    description: str | None = None