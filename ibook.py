
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from checkAuthorization import checking_auth, Сheck_Auth

app = FastAPI()

@app.get("/", response_class=HTMLResponse, tags=["Home"])
async def home():
   with open('Hello.html') as html_file:
        data = html_file.read()
   return HTMLResponse(content = data, status_code = 200)

@app.post("/verification/",  tags=["Authorization|Registration"])
async def authorization_verification(auth: Сheck_Auth):
    return checking_auth(auth.token)

if __name__ == "__main__":
   uvicorn.run("ibook:app", host = "134.0.115.2", port = 80, reload = True)