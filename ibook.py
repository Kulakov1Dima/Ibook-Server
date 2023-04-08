
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from checkAuthorization import checking_auth, Сheck_Auth

app = FastAPI()

file_path = "ibook.apk"

@app.get("/", response_class=HTMLResponse, tags=["Home"])
async def home():
   with open('Hello.html') as html_file:
        data = html_file.read()
   return HTMLResponse(content = data, status_code = 200)

@app.get("/version/",  tags=["Home"])
async def download_app():
    return "2.7.0"

@app.get("/up/",  tags=["Home"])
async def up_app():
    return FileResponse(path=file_path, filename=file_path, media_type='application/octet-stream')

@app.post("/verification/",  tags=["Authorization|Registration"])
async def authorization_verification(auth: Сheck_Auth):
    return checking_auth(auth.token)

if __name__ == "__main__":
   uvicorn.run("ibook:app", host = "134.0.115.2", port = 80, reload = True)