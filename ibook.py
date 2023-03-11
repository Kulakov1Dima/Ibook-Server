
import uvicorn as uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
   uvicorn.run("ibook:app", host="localhost", port=9000, reload=True)