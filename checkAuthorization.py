from pydantic import BaseModel

class Сheck_Auth(BaseModel):
    token: str

def checking_auth(token):
    return True