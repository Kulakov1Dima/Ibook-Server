
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from checkAuthorization import checking_auth, Сheck_Auth, Return_data_verification

app = FastAPI()

file_path = "ibook.apk"
data_base = "../users.db"

@app.get("/", response_class = HTMLResponse, tags = ["Home"])
async def home():
   with open('Hello.html') as html_file:
        data = html_file.read()
   return HTMLResponse(content = data, status_code = 200)

@app.get("/version/",  tags = ["Home"])
async def update_app():
    return "2.6.9"

@app.get("/up/",  tags = ["Home"])
async def download_app():
    return FileResponse(path = file_path, filename = file_path, media_type = 'application/octet-stream')

@app.post("/verification/",  tags = ["Authorization|Registration"], response_model = Return_data_verification)
async def authorization_verification(auth: Сheck_Auth):
    return checking_auth(auth.email, data_base)

@app.post("/registration/", tags = ["Authorization|Registration"])
async def registration():
    return "hello"

if __name__ == "__main__":
   uvicorn.run("ibook:app", host = "134.0.115.2", port = 80, reload = True)