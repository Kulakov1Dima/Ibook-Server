import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse, tags=["Home"], summary="Главная страница сервера", description="Страница авторицации и администратирования", responses={
    200: {"description": "HTML страница успешно открыта"},
    404: {"description": "Страница не доступна"}
})
async def home():
    html_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__))+ '/main_page', 'Hello.html')
    with open(html_file_path) as html_file:
        data = html_file.read()
    return HTMLResponse(content=data, status_code=200)

if __name__ == "__main__":
   uvicorn.run("ibook:app", host="192.168.1.146", port=9000, reload=True,
                ssl_keyfile=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ibook-daa2557bc9hb3.keenetic.pro-privateKey.key'),
                ssl_certfile=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ibook-daa2557bc9hb3.keenetic.pro.crt'))
   #uvicorn.run("ibook:app", host="localhost", port=9000, reload=True, ssl_keyfile="ibook-daa2557bc9hb3.keenetic.pro-privateKey.key", ssl_certfile="ibook-daa2557bc9hb3.keenetic.pro.crt")