
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from checkAuthorization import Auth

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
   with open('Hello.html') as html_file:
        data = html_file.read()
   return HTMLResponse(content = data, status_code = 200)

@app.post("/auth/")
async def create_auth(auth: Auth):
    return auth.description

if __name__ == "__main__":
   uvicorn.run("ibook:app", host = "134.0.115.2", port = 9000, reload = True)