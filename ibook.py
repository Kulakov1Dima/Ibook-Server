import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse, tags=["Home"])
async def home():  # HTML превьюшка
    html_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Hello.html')
    with open(html_file_path) as html_file:
        data = html_file.read()
    return HTMLResponse(content=data, status_code=200)

@app.get("/version/", tags=["Home"])
async def update_app():
    return "2.6.9"  # Текущая актуальная версия приложения до которого будут обновляться старые

if __name__ == "__main__":
   uvicorn.run("ibook:app", host="192.168.1.146", port=9000, reload=True,
                ssl_keyfile=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ibook-daa2557bc9hb3.keenetic.pro-privateKey.key'),
                ssl_certfile=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ibook-daa2557bc9hb3.keenetic.pro.crt'))
   #uvicorn.run("ibook:app", host="localhost", port=9000, reload=True, ssl_keyfile="ibook-daa2557bc9hb3.keenetic.pro-privateKey.key", ssl_certfile="ibook-daa2557bc9hb3.keenetic.pro.crt")