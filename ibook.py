
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

file_path = "ibook.apk"
data_base = "../users.db"

@app.get("/", response_class = HTMLResponse, tags = ["Home"])
async def home():                                                              # HTML превьюшка
   with open('Hello.html') as html_file:
        data = html_file.read()
   return HTMLResponse(content = data, status_code = 200)

@app.get("/version/",  tags = ["Home"])
async def update_app():
    return "2.6.9"                                                             # Текущая актуальная версия приложения до которого будут обновляться старые

if __name__ == "__main__":
   #uvicorn.run("ibook:app", host = "127.0.0.1", port = 80, reload = True)      # Запуск сервера для локальной машины
    uvicorn.run("ibook:app", host = "192.168.1.146",port = 9000, reload = True)