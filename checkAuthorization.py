import sqlite3
from pydantic import BaseModel

class Сheck_Auth(BaseModel):
    email: str

def checking_auth(email, path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return True