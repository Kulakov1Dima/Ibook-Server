import sqlite3
from pydantic import BaseModel

class Сheck_Auth(BaseModel):
    email: str

class Return_data_verification(BaseModel):
    surname: str | None = None
    name: str | None = None
    patronymic: str | None = None
    nickname: str
    age: int
    status: str

def checking_auth(email, path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return Return_data_verification(surname ="null", name = "null", patronymic = "null", nickname = "null", age = 0, status = "DELITED")