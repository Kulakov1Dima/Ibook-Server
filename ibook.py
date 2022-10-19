import uvicorn as uvicorn
from fastapi import FastAPI
application = FastAPI()

@application.get("/")
def root():
   return {"message": "Ibook Server are working for you ;)"}

if __name__ == "__main__":
   uvicorn.run("ibook:application", port=9000, reload=True)