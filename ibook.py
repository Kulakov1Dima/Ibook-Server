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
   uvicorn.run("ibook:app", 
               host="192.168.1.146", 
               port=9000, reload=True, 
               ssl_keyfile="-----BEGIN RSA PRIVATE KEY-----MIIEpAIBAAKCAQEAt8yNIvuG7rl8AZEI8vcJ7OrllBenKMNi9/6uazlsxU4LxpSAITNK7XLI1gxd7YV7r+7lnpa0d5vvb8CNi9NH8DTxtEG71ba3skkX2Jr6QTYOUvGnRWibTTqlr2Q/+UyAJPZBYO1KZPZi3njj/SiyxozPz91cGdQMydVVJXYmYR+EUFYYm5wAnbqE8TM7UHFXzLkEMMYvF9AfV/jGMugC/xRJwdOPK8hlYG0rD6Ltu+BoKuiPrOm1vqnEyYIO10yPYU0dFFIwHa6YARn+7/3ytLsdsqPkpiqBf4PWV8U2i3nFWs9zv6jUpTxtoncxgRZDZDBTI9ylrRN8MEEmnOBXrQIDAQABAoIBAFRhcORAFIzxk+hGNRUSbDicCKUqDMCOnxeakWnBldmpQIe88mwLl9kWSvTV/aNHlmbJZxqdNqH48X5dKL6qU4sIS3UFfp4ZghE0NGHpmH2quv3CWphnc3ELvTgd7q7du7D8azx8BB0A7pgTaRv2/MhhqiBUkG19KBfbPHlz2h/Y57ZT8LaEyceOGSevEd/ONKYbJVG+3+EFGxwQhFP80vteTbvDtK480za9RdE6fF1q8n3fk27yL309HpEbVPonDYB0/Ubc+wQutjA6vH3oFUHlZL3kS/14rT7cZC0JoJ3p3E3z6GsPgL51EsSLHBeAAHfQHZXW5FqrHL1xRugAyCMCgYEA7tETPTfmFcUxH9xXYIAh21/zSuYIWtCTVR7NL+koWha07hIj0pGhLxx2e4BfFtARJCrl+bwL0sX5xRYFga3Z4wdceoskt4neGxMWHJbffD7HiacwC/ijo+acsdl/wzo2bMwGbg/2XgcQ92zCrI7FI9YVIEy8AxYkA7bGRvffs4sCgYEAxQYRnRT8TTFgCqrmfFLM+WqmtxOP6F4mqZVMpddz1Qf/CEkDxG4zzyrQA5tT1skrNrPntGa0VfgMZhLb/rd54gXhUmQhHQhq3QaDB4Dr08CnrDKvWgn+9zqWzgjYz/mOtmduecXE1bwiUlqZYEHDrY4pLLkdJ0rLAhUSIXw9qKcCgYEAr27Y8jyxAccU2jHT4ijeNjgbEic/de8IfBwfYRWnNd6+VLDwrcubG2+OPhVERQ7duLLms/kGunQCklwl+WhLyjHrJn42n7lgdoUj1iaiz7OSgzVU30Zsd4d+DkwXRcPqnSuXgZyqP9JzDT9RFs/eU//9DvgvmRjXpf7LUvDd3RcCgYEArMWboIIMlaycqf4fzBnYAUgTFiwjYANgKAnyguOigcdXT26nzRNOf3btnpwRMyKJsJimsT33GgRA6ynSnVVLnnbFljiUCR+ehl/1exkEtFYXMxvnRS/K1AYexGJhrk8LZMzixgo1h7BI8KreINjKvWESnlNeS1x9FUBg+9g1QbUCgYBb0aHBCgEHoCV11fZY7cPN5tnDmL5J+30OgNMWGP14d+o1tOnRUbzESjElPX3f5t45SeQzxpVrd7SOYPEhC3LagYgW/3X7tWPyKD2EZN8dGlHURpo9EjC5SUXqEVIdrGGG9kSx2Q0u3tfMFCJ0kOG798C1nOrU7liyko7y+d/RAw==-----END RSA PRIVATE KEY-----",
                ssl_certfile=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ibook-daa2557bc9hb3.keenetic.pro.crt"))
   #uvicorn.run("ibook:app", host="localhost", port=9000, reload=True, ssl_keyfile="ibook-daa2557bc9hb3.keenetic.pro-privateKey.key", ssl_certfile="ibook-daa2557bc9hb3.keenetic.pro.crt")